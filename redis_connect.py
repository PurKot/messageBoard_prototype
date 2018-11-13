import redis
import constants

def connectRedis():
    return redis.StrictRedis(host=constants.redis_host,
                                port=constants.redis_port,
                                password=constants.redis_password)
