"""
CLI (Command Line Interface) - command line interface for the app
"""

import argparse
import subprocess
import platform
import socket
from loguru import logger
from utils import Utils
import argparse
import socket
import sys
import os
from loguru import logger
from services import BluetoothServices, NedodropService
from utils import Utils

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['send', 'receive'], help='Type file_paths to send it')
    parser.add_argument('-f', '--file', type=str, nargs='*', help='Type file paths to send them', action='store')


    args = parser.parse_args()
# 1. Turn on Bluetooth
# 2. Start `bluetooth.bind()`
# 3. Get via Bluetooth host and port
# 4. Close Bluetooth socket `bluetooth.close()`
# 5. `nedodrop.connect(host, port)`
# 6. `nedodrop.receive()`
# 7. After exit event `nedodrop.close()`
    if args.action == 'receive':
        # Utils.turn_on_bluetooth()
        # bluetooth = BluetoothServices()
        # bluetooth.bind()
        # host, port = bluetooth.receive_info()
        nedodrop = NedodropService()
        nedodrop.connect(host=socket.gethostbyname(socket.gethostname()), port=8000)
        nedodrop.receive_file()
        # while somebody didn't left
        nedodrop.close()


# 1. Choose file/files
# 2. Turn on Bluetooth
# 3. Start `bluetooth.find`
# 4. Connect using `bluetooth.connect(find)` information
# 5. `nedodrop` = Start socket (to generate host and port)
# 7. Send via Bluetooth host and port
# 8. Close Bluetooth socket `bluetooth.close()`
# 9. `nedodrop.send_file()`
# 10. After exit event `nedodrop.close()`
    elif args.action == 'send':
        if args.file is None:
            parser.error("Need -f,--file when using send")
        if not os.path.isfile(args.file[0]):
            parser.error("File in -f,--file not found")
        else:
            file = args.file
        # Utils.turn_on_bluetooth()
        # bluetooth = BluetoothServices()
        # devices = bluetooth.find()
        # bluetooth.connect(devices[0]['bmac'], 4)
        # bluetooth.send_info()
        # choosing from list for a device
        nedodrop = NedodropService()
        # bluetooth.send_info(nedodrop.host, nedodrop.port)
        nedodrop.bind()
        nedodrop.send_file(file_path=file[0])
        
        nedodrop.close()
        

if __name__ == "__main__":
    main(sys.argv[1:])