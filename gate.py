# -*- coding: UTF-8 -*-

from base.server.gate_server import GateServer


if __name__ == "__main__":
    temp_logic = GateServer("local")
    server_info = temp_logic.get_server_data("GateServer")
    temp_logic.start_run(host=server_info["ip"], port=server_info["port"])

