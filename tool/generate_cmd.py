# -*- coding: utf-8 -*-

import json

CMD_LIST = {
    "RegisterReq": 1,
    "RegisterRsp": 2,
    "LoginReq": 3,
    "LoginRsp": 4,
    "GameServerInfoReq": 5,
    "GameServerInfoRsp": 6,
    "RoleDataGetReq": 7,
    "RoleDataGetRsp": 8,
}

if __name__ == "__main__":
    temp_list = {}
    for key, value in CMD_LIST.items():
        temp_list[key] = value
    with open("../doc/cmd/cmd.json", "w") as fo:
        temps = json.dumps(temp_list)
        fo.write(temps)
