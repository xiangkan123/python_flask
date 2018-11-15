# -*- coding: utf-8 -*-
import json
import os

from log.log_manager import Log


class MapMethod(object):

    @classmethod
    def init(cls):
        cls.load_module()
        cls.get_map_class()

    @classmethod
    def load_module(cls):
        dir_path = "app/action"
        path = "app.action."
        cls.module_list = list()
        file_list = os.listdir(dir_path)
        for _file in file_list:
            if not _file.startswith('act') or not _file.endswith("py"):
                continue
            _file = _file[0: -3]
            cls.module_list.append(__import__(path + _file, fromlist=True))

    @classmethod
    def get_map_class(cls):
        cls.map_class = {}
        for _module in cls.module_list:
            with open("doc/cmd/cmd.json", "r") as fo:
                temp_data = json.loads(fo.read())
                for key, value in temp_data.items():
                    pos = key.find("Req")
                    if pos != -1:
                        temp_key = key[0: -3]
                        _class = getattr(_module, temp_key, None)
                        if not _class:
                            continue
                        cls.map_class[value] = _class()

    @classmethod
    def get_class(cls, key):
        try:
            _class = cls.map_class[key]
        except Exception as e:
            Log.error("without found method error - > {0}".format(e))
            return None
        return _class
