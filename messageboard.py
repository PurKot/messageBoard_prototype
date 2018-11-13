from utilities import messageboarddb
from utilities import redis_pub
from utilities import redis_sub

import pymongo
import time
from pymongo import CursorType

class messageBoardApp:

    def __init__(self):
         self.messageboarddb = messageboarddb
         self.channel = None
         self.listen = None
         self.messageBoardSel = False
         self.watchCursor = False
         self.stopListenFlag = False


def createMsgBoard(messageBoardApp,name):
    messageBoardApp.messageboard = messageboarddb.create_collection(name)

def showboards():
    listBoards = messageboarddb.list_collection_names()
    print(f'existing boards: {listBoards}')
    print('chose an existing board or create a new board with select command')

def select(messageboardApp,board_name):
    messageBoardApp.channel = board_name
    listBoards = messageboarddb.list_collection_names()
    if board_name in listBoards:
        messageboardApp.messageBoardSel= messageboarddb.get_collection(board_name)
        print(board_name +" selected")
    else:
        createMsgBoard(messageboardApp,board_name)
        messageboardApp.messageBoardSel = messageboarddb.get_collection(board_name)

def read(messageboardApp):
    if messageboardApp.messageBoardSel != False:
        for x in messageboardApp.messageBoardSel.find({},{ "message": 1 }):
            print(x["message"])
    else:
        print("No board Selected. Use select <board> to select a message board before read")

def write(messageboardApp,message):
    doc = {
        "message": message
    }
    if messageboardApp.messageBoardSel != False:
        messageboardApp.messageBoardSel.insert(doc)
        write_to_redis(messageBoardApp, message)
    else:
        print("No board Selected. Use select <board> to select a message board before write")

def write_to_redis(messageBoardApp, message):
    redis_pub.publish(messageBoardApp.channel, message)

def listen(messageboardApp):
    if messageboardApp.messageBoardSel != False:
        print(f'listening on {messageBoardApp.channel}')
        redis_sub.subscribe(**{messageBoardApp.channel: print_redis_message})
        messageBoardApp.listen = redis_sub.run_in_thread(sleep_time=0.001)
    else:
        print("No board Selected. Use select <board> to select a message board before read")

def print_redis_message(message):
    print(message['data'].decode('utf-8'))

def stop(messageboardApp):
    messageBoardApp.listen.stop()
    redis_sub.unsubscribe(messageBoardApp.channel)
