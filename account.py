# -*- coding: UTF-8 -*-

from base.server.account_server import AccountServer


if __name__ == "__main__":
    temp_logic = AccountServer("local")
    server_info = temp_logic.get_server_data("AccountServer")
    temp_logic.start_run(host=server_info["ip"], port=server_info["port"])

