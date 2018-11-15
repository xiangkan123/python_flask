# -*- coding: utf-8 -*-
"""
    content login component
    date 2018 - 11 - 12
    author cy-h
"""

from db.db_manager import DBManager
from db.db_table_config import DBTableConfig


def get_role_data(role_id):
    """
    获得角色数据
    :param role_id:
    :return:
    """
    role_data = DBManager.get_record(DBTableConfig.table_role_data, {"role_id": role_id})
    return role_data


def create_role(role_id):
    """
    创建角色
    :param role_id:
    :return:
    """
    role_data = {"role_id": role_id, "name": "1", "lv": 1, "exp": 0, "vitality": 100, "diamond": 0, "gold": 0}
    DBManager.insert_record(DBTableConfig.table_role_data, role_data)
    return role_data


def get_login_data(req):
    """

    :param req:
    :return:
    """
    role_id = req["role_id"]
    role_data = get_role_data(role_id)

    if not role_data:
        role_data = create_role(role_id)
    role_data["code"] = 0
    return role_data
