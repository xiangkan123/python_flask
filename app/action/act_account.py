# -*- coding: utf-8 -*-
"""
    content act account
    date 2018 - 11 - 12
    author cy-h
"""

from base.act_base import ActBase
from app.component.account_component import get_register_result, get_login_result


class Register(ActBase):
    """
    注册账号
    """
    def do(self, req):
        return get_register_result(req)


class Login(ActBase):
    """
    登入
    """
    def do(self, req):
        return get_login_result(req)


class RoleDataGet(ActBase):
    """
    角色数据
    """
    def do(self, req):
        return ""
