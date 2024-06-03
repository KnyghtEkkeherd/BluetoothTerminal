# Bluetooth-communication interface API functions

import simplepyble as bt

# Store the adapters as a global variable
adapters = []
peripherals = []
adapter = 0
peripheral = 0

def bt_getAdapter():
    global adapters, adapter
    adapters = bt.Adapter.get_adapters()
    if len(adapters) == 0:
        print("No adapters found")
        return -1
    
    print("Please select an adapter:")
    for i, adapter in enumerate(adapters):
        print(f"{i}: {adapter.identifier()} [{adapter.address()}]")

    choice = int(input("Enter choice: "))
    adapter = adapters[choice]
    
    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
    adapter.set_callback_on_scan_found(lambda peripheral: print(f"Found {peripheral.identifier()} [{peripheral.address()}]"))

    print(f"Selected adapter: {adapter.identifier()} [{adapter.address()}]")
    
    return 0

def bt_scan():
    # Scan for 5 seconds
    global peripherals, adapter
    adapter.scan_for(5000)
    peripherals = adapter.scan_get_results()
    
def bt_connect():
    global peripherals, peripheral
    # Query the user to pick a peripheral
    print("Please select a peripheral:")
    for i, peripheral in enumerate(peripherals):
        print(f"{i}: {peripheral.identifier()} [{peripheral.address()}]")

    choice = int(input("Enter choice: "))
    peripheral = peripherals[choice]
    
    print(f"Connecting to: {peripheral.identifier()} [{peripheral.address()}]")
    peripheral.connect()

    print("Successfully connected, listing services...")
    services = peripheral.services()
    for service in services:
        print(f"Service: {service.uuid()}")
        for characteristic in service.characteristics():
            print(f"    Characteristic: {characteristic.uuid()}")

def bt_disconnect():
    if (peripheral):
        peripheral.disconnect()
    else:
        print("No peripheral to disconnect!")