# -*- coding: UTF-8 -*-

"""
打印日志文件
"""


class Log(object):
    dir="log/"
    _file = None

    @classmethod
    def init(cls, file_name):
        cls._file = file_name

    @classmethod
    def error(cls, data):
        print "/****************************************************************" \
                "{0}"\
              "*****************************************************************/".format(data)

    @classmethod
    def logger(cls, data):
        print "/****************************************************************" \
                "{0}"\
              "*****************************************************************/".format(data)