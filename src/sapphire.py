import keyboard
import pymem
import pymem.process
import time
from config import *

pm = pymem.Pymem("csgo.exe")


def main():
    print("Sapphire has launched. Your trigger key is: {}.".format(aim_key))

    client = pymem.process.module_from_name(pm.process_id, "client.dll")
    player = client.base_address + dwLocalPlayer
    in_crosshair = pm.read_int(player) + m_iCrosshairId
    force_attack = client.base_address + dwForceAttack

    while True:
        result = pm.read_int(in_crosshair)

        if keyboard.is_pressed(aim_key):
            if result > 0 and result <= 64:
                pm.write_int(force_attack, 5)
                time.sleep(0.01)  # Revolver won't fire without delay.
                pm.write_int(force_attack, 4)


if __name__ == '__main__':
    main()
