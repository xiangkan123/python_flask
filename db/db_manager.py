# -*- coding: utf-8 -*-

"""
    数据库管理
    date 2018-8-1
    author cy-h
"""
import pymysql

import db_util
from log.log_manager import Log


class DBManager(object):

    _db = None

    @classmethod
    def connect(cls, params):
        cls._db = pymysql.connect(params["ip"], 'root', 'root', "user", charset='utf8')
        Log.logger("connect sql success! ")

    @classmethod
    def create_table(cls, table_name):
        """

        :param table_name:
        :return:
        """
        if not cls._db:
            return

        cursor = cls._db.cursor()
        try:
            cursor.execute("DROP TABLE IF EXISTS %s" % table_name)
        except Exception as e:
            Log.logger("drop table data error {0}".format(e))
            return

        temp_sql = db_util.get_table_sql(table_name)
        try:
            cursor.execute(temp_sql)
            Log.logger("create table success !")
        except Exception as e:
            Log.error("create table error {0}".format(e))

    @classmethod
    def insert_record(cls, table_name, params, reset=False):
        """
        :param table_name:
        :param params:
        :param reset:
        :return:
        """
        if not cls._db:
            return
        cursor = cls._db.cursor()
        if not cursor.execute("show tables like \'%s\'" % table_name):
            cls.create_table(table_name)
        if reset:
            cls.create_table(table_name)

        temp_sql = db_util.get_insert_sql(table_name, params)
        try:
            cursor.execute(temp_sql)
            cls._db.commit()
            Log.logger("insert data success !")
        except Exception as e:
            Log.error("inert data error {0}".format(e))
            cls._db.rollback()
            return False
        return True

    @classmethod
    def get_record(cls, table_name, params):
        """

        :param table_name:
        :param params:
        :return:
        """
        if not cls._db:
            return
        cursor = cls._db.cursor()
        temp_sql = db_util.get_record_sql(table_name, params)
        try:
            cursor.execute(temp_sql)
            result = cursor.fetchall()
        except Exception as e:
            Log.error("get data error {0}".format(e))
            cls._db.rollback()
            return
        Log.logger("get data success !")
        if not result:
            return
        return db_util.deal_get_result(table_name, result[0])

    @classmethod
    def update_record(cls, table_name, params, field, value):
        """

        :param table_name:
        :param params:
        :param field:
        :param value:
        :return:
        """
        if not cls._db:
            return
        cursor = cls._db.cursor()
        temp_sql = db_util.get_update_sql(table_name, params, field, value)
        try:
            cursor.execute(temp_sql)
            cls._db.commit()
        except Exception as e:
            Log.error("update data error {0}".format(e))
            cls._db.rollback()
            return
        Log.logger("update data success !")

    @classmethod
    def delete_record(cls, table_name, params):
        """

        :param table_name:
        :param params:
        :return:
        """
        if not cls._db:
            return
        cursor = cls._db.cursor()
        temp_sql = db_util.get_del_sql(table_name, params)
        try:
            cursor.execute(temp_sql)
            cls._db.commit()
        except Exception as e:
            Log.error("delete data error {0}".format(e))
            cls._db.rollback()
            return
        Log.logger("delete data success !")

    @classmethod
    def close_db(cls):
        if not cls._db:
            return
        cls.db.close()
