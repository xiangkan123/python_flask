# -*- coding: UTF-8 -*-

import protocol.protocol as protocol
from flask import Flask, request
from base.manager.require_manager import RequireManager

app = Flask(__name__)


@app.route(protocol.register, methods=['POST'])
def register():
    return RequireManager.require_responses(request.data)


@app.route(protocol.login, methods=['POST'])
def login():
    return RequireManager.require_responses(request.data)


@app.route(protocol.logout, methods=['GET'])
def logout():
    return "logout"


class StartRoute(object):

    def __init__(self, host, port):
        app.run(host=host, port=port)
