# -*- coding: UTF-8 -*-

"""
    content account server
    date 2018 - 10 - 30
    author cy-h
"""

from base.manager.redis_manager import RedisManager
from base_server import BaseServer
from db.db_manager import DBManager
from log.log_manager import Log
from route.account_route import StartRoute


class AccountServer(BaseServer):

    def __init__(self, config_name):
        self.init(config_name)
        self.load()

    def load(self):
        Log.init("logic")

        DBManager.connect(self.get_server_data("DBServer"))
        RedisManager.init(self.get_server_data("RedisServer"))

    @classmethod
    def start_run(cls, host, port):
        StartRoute(host, port)



