# Bluetooth interface terminal
import simplepyble as bt
import bt_utils

is_quit = False
is_calibrated = 0

while (not is_quit):
    choice = int(input(f"""
                       || Options:
                       || [0] Get Adapter
                       || [1] Scan nearby devices
                       || [2] Connect to a device
                       || [3] Quit\n"""))
    match choice:
        case 0:
            bt_utils.bt_getAdapter()
            is_calibrated += 1
            continue
        case 1:
            if (is_calibrated > 0):
                bt_utils.bt_scan()
                is_calibrated += 1
            else:
                print("Get adapter first!")
            continue
        case 2:
            if (is_calibrated >= 2):
                bt_utils.bt_connect()
            elif (is_calibrated == 1):
                print("Scan before connecting!")
            else:
                print("Get adapter first!")
            continue
        case 3:
            is_quit = True
            continue
        case _:
            continue

bt_utils.bt_disconnect()
print("Exiting the programme...")