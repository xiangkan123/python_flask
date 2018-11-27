# -*- coding: UTF-8 -*-
"""
    content require manager
    date 2018 - 11 - 12
    auth cy-h
"""
import json
import tool.error_code as code
from tool.map_method import MapMethod
from token_manager import ToKenManager


no_token_list = [1, 3, 5]


class RequireManager (object):

    @classmethod
    def require_responses(cls, params):
        rsp_data = {"code": 0}
        temp_data = json.loads(params.data)
        headers = params.headers
        cmd = temp_data["cmd"]
        # 不是登入的情况
        if cmd not in no_token_list and not ToKenManager.check_token(temp_data["role_id"], headers["Content-Type"]):
            rsp_data["code"] = code.TOKEN_DATA_ERROR
        else:
            _class = MapMethod.get_class(cmd)
            if not _class:
                rsp_data["code"] = code.METHOD_NOT_FOUND
            else:
                rsp_data = _class.take(temp_data)
        return json.dumps(rsp_data)
