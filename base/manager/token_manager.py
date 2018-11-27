# -*- coding: UTF-8 -*-

import time
import base64
from log.log_manager import Log


class ToKenManager(object):

    @classmethod
    def general_token(cls, key, expire=3600):
        ts_str = str(int(time.time()) + expire)
        ts_byte = ts_str + ":{0}".format(key)
        b64_token = base64.b64encode(ts_byte)
        return b64_token

    @classmethod
    def check_token(cls, key, token):
        try:
            ts_byte = base64.b64decode(token)
        except Exception as e:
            Log.error("token without find {0}".format(e))
            return False

        temp_list = ts_byte.split(':')
        curr_time = int(time.time())
        origin_time = int(temp_list[0])

        if key != temp_list[1]:
            return False

        if origin_time > curr_time:
            return True
        return False
