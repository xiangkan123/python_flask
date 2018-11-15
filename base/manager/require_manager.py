# -*- coding: UTF-8 -*-
"""
    content require manager
    date 2018 - 11 - 12
    auth cy-h
"""
import json
import tool.error_code as code
from tool.map_method import MapMethod


class RequireManager (object):

    @classmethod
    def require_responses(cls, params):
        temp_data = json.loads(params)
        cmd = temp_data["cmd"]
        rsp_data = {"code": 0}
        _class = MapMethod.get_class(cmd)
        if not _class:
            rsp_data["code"] = code.METHOD_NOT_FOUND
        else:
            rsp_data = _class.take(temp_data)
        return json.dumps(rsp_data)
