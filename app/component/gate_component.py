# -*- coding: utf-8 -*-
"""
    content gate component
    date 2018 - 11 - 12
    author cy-h
"""
from base.manager.config_manager import ConfigManager


def get_server_info(req):
    """

    :param req:
    :return:
    """
    temp_data = {"LogicServer": ConfigManager.get_server_data("LogicServer"),
                 "AccountServer":  ConfigManager.get_server_data("AccountServer")}
    return temp_data
