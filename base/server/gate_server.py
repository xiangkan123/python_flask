# -*- coding: UTF-8 -*-

"""
    content logic server
    date 2018 - 10 - 30
    author cy-h
"""

from base.manager.redis_manager import RedisManager
from base_server import BaseServer
from db.db_manager import DBManager
from log.log_manager import Log
from route.gate_route import StartRoute
from tool.map_method import MapMethod


class GateServer(BaseServer):

    def __init__(self, config_name):
        self.init(config_name)
        self.load()

    def load(self):
        Log.init("gate")

        DBManager.connect(self.get_server_data("DBServer"))
        RedisManager.init(self.get_server_data("RedisServer"))
        MapMethod.init()

    @classmethod
    def start_run(cls, host, port):
        StartRoute(host, port)


