# -*- coding: UTF-8 -*-

import json


class JsonLoad(object):

    cmd_dict = dict()

    @classmethod
    def load_file(cls):
        with open("../doc/cmd/cmd.json", "r") as fo:
            cls.cmd_dict = json.loads(fo.read())

    @classmethod
    def get_items(cls):
        return cls.cmd_dict

    @classmethod
    def get_value(cls, key):
        return cls.cmd_dict[key]
