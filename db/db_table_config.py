# -*- coding: utf-8 -*-

"""
    数据库表格
    date 2018-8-1
    author cy-h
"""


class DBTableConfig(object):
    table_user_data = "user_data"
    table_account_data = "account_data"
    table_role_data = "role_data"
    table_item_data = "item_data"
    table_section_data = "section_data"

    db_list = {
        table_user_data: ["role_id", "user_id"],
        table_account_data: ["account", "password", "role_id", "ban"],
        table_role_data: ["role_id", "name", "lv", "exp", "vitality", "diamond", "gold"]
    }
