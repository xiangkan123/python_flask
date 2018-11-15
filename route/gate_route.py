# -*- coding: UTF-8 -*-

import protocol.protocol as protocol
from flask import Flask, request
from base.manager.require_manager import RequireManager

app = Flask(__name__)


@app.route(protocol.server_info_get, methods=['POST'])
def get_role_data():
    return RequireManager.require_responses(request.data)


class StartRoute(object):

    def __init__(self, host, port):
        app.run(host=host, port=port)
