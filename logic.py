# -*- coding: UTF-8 -*-

from base.logic_server import app, LogicServer


if __name__ == "__main__":
    temp_logic = LogicServer("local")
    server_info = temp_logic.get_server_data("LogicServer")
    app.run(host=server_info["ip"], port=server_info["port"])
