# -*- coding: utf-8 -*-
from db_table_config import DBTableConfig


def get_where_sql(params):
    temp_where = ""
    for key, value in params.items():
        if temp_where != "":
            temp_where += " and "
        if isinstance(value, int):
            temp_where += key + "=%d" % value
        else:
            temp_where += key + "=\'" + value + '\''
    return temp_where


def get_account_data(table_name):
    return "create table %s(" \
            "account VARCHAR(20) PRIMARY KEY NOT NULL, " \
            "password VARCHAR(20) NOT NULL, " \
            "user_id VARCHAR(30) NOT NULL," \
            "ban INT NOT NULL " \
           ");" % table_name


def get_user_data(table_name):
    sql = "create table %s( " \
          "role_id VARCHAR (30) NOT NULL," \
          "user_id VARCHAR (30) PRIMARY KEY NOT NULL);" % table_name
    return sql


def get_role_data(table_name):
    sql = "create table %s( " \
          "role_id VARCHAR (30) PRIMARY KEY NOT NULL," \
          "name VARCHAR (20) NOT NULL ," \
          "lv INT NOT  NULL ," \
          "exp INT NOT NULL ," \
          "vitality INT NOT NULL," \
          "diamond INT NOT NULL," \
          "gold INT NOT NULL);" % table_name
    return sql


def get_table_sql(table_name):
    if DBTableConfig.table_user_data == table_name:
        sql = get_user_data(table_name)
    elif DBTableConfig.table_account_data == table_name:
        sql = get_account_data(table_name)
    elif DBTableConfig.table_role_data == table_name:
        sql = get_role_data(table_name)
    return sql


def get_insert_sql(table_name, params):
    temp_data, temp_value = "", ""
    value_list = DBTableConfig.db_list[table_name]
    for _value in value_list:
        temp_data = temp_data + _value
        if isinstance(params[_value], int):
            temp_value += "{0}"
            temp_value = temp_value.format(params[_value])
        else:
            temp_value = temp_value + '\'' + params[_value] + '\''
        if _value != value_list[-1]:
            temp_data += ","
            temp_value += ","
    sql = "insert into %s (%s) values (%s)" % (table_name, temp_data, temp_value)
    return sql


def get_record_sql(table_name, params):
    temp_where = get_where_sql(params)
    sql = "select * from %s where %s" % (table_name, temp_where)
    return sql


def get_update_sql(table_name, params, field, value):
    """

    :param table_name:
    :param params:
    :param field:
    :param value:
    :return:
    """
    temp_where = get_where_sql(params)
    if isinstance(value, int):
        temp_value = "%s=%d" % (field, value)
    else:
        temp_value = "%s=\'%s\'" % (field, value)
    return "update %s set %s where %s" % (table_name, temp_value, temp_where)


def get_del_sql(table_name, params):
    """

    :param table_name:
    :param params:
    :return:
    """
    temp_where = get_where_sql(params)
    return "delete from %s where %s" % (table_name, temp_where)


def deal_get_result(table_name, params):
    """

    :param table_name:
    :param params:
    :return:
    """
    name_list = DBTableConfig.db_list[table_name]
    temp_data = {}
    for index, name in enumerate(name_list):
        temp_data[name] = params[index]
    return temp_data
