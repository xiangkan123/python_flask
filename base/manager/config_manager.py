# -*- coding: UTF-8 -*-

"""
    content config manager
    date 2018 - 10 - 30
    author cy-h
"""


class ConfigManager(object):
    _dir = "config/"
    server_dict = dict()

    @classmethod
    def load(cls, config_name=None):
        if not config_name:
            return
        with open(cls._dir + config_name, "r") as f:
            server_name, once, index = None, 0, 0
            while True:
                temp = f.readline()
                pos = temp.find("[")
                if pos != -1:
                    server_name = temp.strip('[').rstrip(']\n')
                    cls.server_dict[server_name] = {}
                    continue

                pos = temp.find('=')
                if pos != -1:
                    key = temp[0: pos - 1]
                    value = temp[pos + 2: len(temp) - 1]
                    if key == "port":
                        value = int(value)
                    cls.server_dict[server_name][key] = value
                    index = 0
                else:
                    index += 1

                if index > 2:
                    break

    @classmethod
    def get_server_data(cls, server_name):
        if server_name in cls.server_dict:
            return cls.server_dict[server_name]
        return None



