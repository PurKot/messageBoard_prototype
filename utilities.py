from mongo_connect import connectMongo
from redis_connect import connectRedis
import constants
import pymongo
from pymongo import errors as pymonerr

messageboarddb = connectMongo()

redis_pub = connectRedis()
redis_sub = redis_pub.pubsub()
# redis_sub.subscribe("test-redispy")
