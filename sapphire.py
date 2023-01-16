import keyboard
import pymem
import pymem.process
import time
from win32gui import GetWindowText, GetForegroundWindow

ENTITY_LIST_ADDRESS = (0x4D4B104)
FORCE_ATTACK_ADDRESS = (0x317C6EC)
LOCAL_PLAYER_ADDRESS = (0xD36B94)
PLAYER_FLAGS_OFFSET = (0x104)
CROSSHAIR_ID_OFFSET = (0xB3D4)
PLAYER_TEAM_OFFSET = (0xF4)

TRIGGER_KEY = "shift"


def main():
    print("Sapphire has launched.")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        if not keyboard.is_pressed(TRIGGER_KEY):
            time.sleep(0.1)

        if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
            continue

        if keyboard.is_pressed(TRIGGER_KEY):
            local_player = pm.read_int(client + LOCAL_PLAYER_ADDRESS)
