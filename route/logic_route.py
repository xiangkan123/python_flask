# -*- coding: UTF-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"


class StartRoute(object):

    def __init__(self, host, port):
        app.run(host=host, port=port)
