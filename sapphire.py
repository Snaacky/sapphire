import keyboard
import pymem
import pymem.process
import time
from win32gui import GetWindowText, GetForegroundWindow

dwEntityList = (0x4D43AB4)
dwForceAttack = (0x3175088)
dwLocalPlayer = (0xD2FB84)
m_fFlags = (0x104)
m_iCrosshairId = (0xB3D4)
m_iTeamNum = (0xF4)

trigger_key = "shift"


def main():
    print("Sapphire has launched.")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll

    while True:
        if GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
            player = pm.read_int(client + dwLocalPlayer)

            if not keyboard.is_pressed(trigger_key):
                time.sleep(0.1)

            if keyboard.is_pressed(trigger_key):
                entity_id = pm.read_int(player + m_iCrosshairId)
                entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

                entity_team = pm.read_int(entity + m_iTeamNum)
                player_team = pm.read_int(player + m_iTeamNum)

                if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                    pm.write_int(client + dwForceAttack, 6)

                time.sleep(0.006)


if __name__ == '__main__':
    main()
