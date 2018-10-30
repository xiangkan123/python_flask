# -*- coding: UTF-8 -*-

"""
    content logic server
    date 2018 - 10 - 30
    author cy-h
"""

from flask import Flask
from base_server import BaseServer
from log.log_manager import Log
from db.db_manager import DBManager

app = Flask(__name__)


class LogicServer(BaseServer):

    def __init__(self, config_name):
        self.init(config_name)
        self.load()

    def load(self):
        Log.init("logic")

        DBManager.connect(self.get_server_data("DBServer"))


@app.route('/')
def index():
    return "hello world"
