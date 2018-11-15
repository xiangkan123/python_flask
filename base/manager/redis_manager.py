# -*- coding: UTF-8 -*-

import redis

from log.log_manager import Log


class RedisManager(object):
    r = None

    @classmethod
    def init(cls, params):
        db = int(params["db"])
        password = params["password"]
        if params["auth"] == "False":
            pool = redis.ConnectionPool(host=params["ip"], port=params["port"], db=db)
        else:
            pool = redis.ConnectionPool(host=params["ip"], port=params["port"], db=db, password=password)
        r = redis.Redis(connection_pool=pool)
        cls.r = r
        Log.logger("init redis")

    @classmethod
    def catch_set(cls, key, value, ex=None):
        cls.r.set(key, value, ex)

    @classmethod
    def catch_get(cls, key):
        return cls.r.get(key)

    @classmethod
    def catch_set_pipe(cls, key, params):
        pipe = cls.r.pipeline(transaction=True)
        for _data in params:
            cls.r.set(key, _data)
        pipe.execute()
