# -*- coding: utf-8 -*-
"""
    content act account
    date 2018 - 11 - 12
    author cy-h
"""

from base.act_base import ActBase
from app.component.login_component import get_login_data


class RoleDataGet(ActBase):
    """
    角色数据
    """
    def do(self, req):
        return get_login_data(req)

