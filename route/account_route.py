# -*- coding: UTF-8 -*-

import protocol.protocol as protocol
from flask import Flask

app = Flask(__name__)


@app.route(protocol.register, methods=['GET'])
def register():
    return "hello world"


@app.route(protocol.register, methods=['GET'])
def login():
    return "login"


@app.route(protocol.register, methods=['GET'])
def logout():
    return "logout"


class StartRoute(object):

    def __init__(self, host, port):
        app.run(host=host, port=port)
