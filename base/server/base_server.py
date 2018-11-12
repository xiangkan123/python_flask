# -*- coding: UTF-8 -*-

"""
    content base server
    date 2018 - 10 - 30
    author cy-h
"""
from base.manager.config_manager import ConfigManager


class BaseServer(object):
    @staticmethod
    def init(config_name):
        print "start server !"
        ConfigManager.load(config_name)

    @staticmethod
    def get_server_data(server_name):
        return ConfigManager.get_server_data(server_name)
