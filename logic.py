# -*- coding: UTF-8 -*-

from base.server.logic_server import LogicServer


if __name__ == "__main__":
    temp_logic = LogicServer("local")
    server_info = temp_logic.get_server_data("LogicServer")
    temp_logic.start_run(host=server_info["ip"], port=server_info["port"])

