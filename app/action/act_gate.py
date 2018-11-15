# -*- coding: utf-8 -*-
"""
    content act account
    date 2018 - 11 - 12
    author cy-h
"""

from base.act_base import ActBase
from app.component.gate_component import get_server_info


class GameServerInfo(ActBase):
    """
    注册账号
    """
    def do(self, req):
        return get_server_info(req)


