# -*- coding: utf-8 -*-
"""
    content account component
    date 2018 - 11 - 14
    author cy-h
"""
import tool.error_code as code
from db.db_manager import DBManager
from db.db_table_config import DBTableConfig
from base.manager.redis_manager import RedisManager
from app.constant.account import ACCOUNT_INIT_VALUE, ACCOUNT_UUID_FLAG
from base.manager.token_manager import ToKenManager


def get_register_result(req):
    """
    处理注册结果
    :param req:
    :return:
    """
    account = req["account"]
    password = req["password"]

    account_data = DBManager.get_record(DBTableConfig.table_account_data, {"account": account})
    if account_data:
        return {"code": code.ACCOUNT_ALREADY_REGISTER}

    account_uuid = RedisManager.catch_get(ACCOUNT_UUID_FLAG)
    if not account_uuid:
        account_uuid = ACCOUNT_INIT_VALUE

    account_data = {"account": account, "password": password, "role_id": str(account_uuid), "ban": 0}
    DBManager.insert_record(DBTableConfig.table_account_data, account_data)

    account_uuid += 1
    RedisManager.catch_set(ACCOUNT_UUID_FLAG, account_uuid)
    return {"code": 0}


def get_login_result(req):
    """
    获得登入数据
    :param req:
    :return:
    """
    account = req["account"]
    password = req["password"]
    account_data = DBManager.get_record(DBTableConfig.table_account_data, {"account": account, "password": password})

    if not account_data:
        return {"code": code.ACCOUNT_PASSWORD_ERROR}

    role_id = account_data["role_id"]
    token = ToKenManager.general_token(role_id)

    return {"role_id": role_id, "code": 0, "token": token}

