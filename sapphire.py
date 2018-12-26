import keyboard
import pymem
import pymem.process

dwEntityList = (0x4CCDBFC)
dwForceAttack = (0x30FF2A0)
dwLocalPlayer = (0xCBD6B4)
m_fFlags = (0x104)
m_iCrosshairId = (0xB394)
m_iTeamNum = (0xF4)

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll
trigger_key = "shift"

def main():
    print("Sapphire has launched.")
    shooting = False
    while True:
        player = pm.read_int(client + dwLocalPlayer)

        if keyboard.is_pressed(trigger_key):
            entity = pm.read_int(player + m_iCrosshairId)

            if entity > 0 and entity <= 64:
                entity = pm.read_int(client + dwEntityList + (entity -1) * 0x10)
                entity_team = pm.read_int(entity + m_iTeamNum)
                player_team = pm.read_int(player + m_iTeamNum)
                    
                if player_team != entity_team:
                    shooting = True
                    pm.write_int(client + dwForceAttack, 5)
            
        if not keyboard.is_pressed(trigger_key) and shooting == True:
            pm.write_int(client + dwForceAttack, 4)
            shooting = False

if __name__ == '__main__':
    main()