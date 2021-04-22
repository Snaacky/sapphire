import json
import pymem
import keyboard
import http.client
from win32gui import GetWindowText, GetForegroundWindow

conn = http.client.HTTPSConnection("raw.githubusercontent.com")
conn.request("GET", "/frk1/hazedumper/master/csgo.json")
values = json.loads(conn.getresponse().read().decode('utf-8'))
conn.close()

dwEntityList = values['signatures']['dwEntityList']
dwForceAttack = values['signatures']['dwForceAttack']
dwLocalPlayer = values['signatures']['dwClientState'] + values['signatures']['dwClientState_GetLocalPlayer'] # check docs for more info
m_fFlags = values['netvars']['m_fFlags']
m_iCrossHairID = values['netvars']['m_iCrosshairId']
m_iTeamNum = values['netvars']['m_iTeamNum']

trigger_key = "shift"


def main():
    print("Sapphire has launched.")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        if not keyboard.is_pressed(trigger_key):
            time.sleep(0.1)

        if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
            continue

        if keyboard.is_pressed(trigger_key):
            player = pm.read_int(client + dwLocalPlayer)
            entity_id = pm.read_int(player + m_iCrosshairId)
            entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

            entity_team = pm.read_int(entity + m_iTeamNum)
            player_team = pm.read_int(player + m_iTeamNum)

            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                pm.write_int(client + dwForceAttack, 6)

            time.sleep(0.006)


if __name__ == '__main__':
    main()
