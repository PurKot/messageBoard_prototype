from messageboard import messageBoardApp
import messageboard

import argparse
import cmd
import string, sys

class cli(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.messageboard1 = messageBoardApp()
        self.prompt='>'

    #implement select command
    def do_showboards(self, arg):
        messageboard.showboards()

    def help_showboards(self):
        print("syntax: showboards")
        print("-- Shows all existing Message boards")

    def do_select(self,boardName):
        messageboard.select(self.messageboard1,boardName)

    def help_select(self):
        print("syntax: select [Board name]")
        print("-- Selects a Message board")

    def do_read(self,arg):
        messageboard.read(self.messageboard1)

    def help_read(self,arg):
        print("syntax: read")
        print("-- Reads from pre selected Message board")

    def do_write(self,message):
        messageboard.write(self.messageboard1,message)

    def help_write(self, message):
        print("syntax: write [Message]")
        print("-- Writes to a Message board")

    def do_listen(self,arg):
        messageboard.listen(self.messageboard1)

    def help_listen(self,arg):
        print("syntax: listen")
        print("-- Listens to updates on a Message board")


    def do_stop(self,arg):
        messageboard.stop(self.messageboard1)

    def help_stop(self,arg):
        print("syntax: stop")
        print("-- Stops listening to a Message board")


    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self,arg):
        print("syntax: quit")
        print("-- terminates the application")

    # shortcuts
    do_q = do_quit




def main():
    cliapp = cli()
    cliapp.cmdloop()


if __name__ == '__main__':
    main()
