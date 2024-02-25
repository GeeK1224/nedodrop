"""
This utils file only compatible with linux for now.
"""

import subprocess
import platform
from loguru import logger

logger.add("client.log", format="{time:YYYY-MM-DD at HH:mm:ss}- {module} - {level} - {message}", level="DEBUG")

class Utils:
    """
    This class contains utility functions.
    """

    def turn_on_bluetooth():
        """
        Toggle Bluetooth
        """
        try:
        # Run rfkill to unblock Bluetooth
            subprocess.run(['rfkill', 'unblock', 'bluetooth'], check=True)
            logger.info("Bluetooth turned on successfully")

        except subprocess.CalledProcessError as e:
            logger.error(f"Error turning on Bluetooth: {e}")

    def get_bluetooth_mac_address():
        '''
        Getting your own Bluetooth Address.
        '''
        result = subprocess.run(["bluetoothctl", "list"], capture_output=True, text=True, check=True)
        mac_address = result.stdout.split(' ')[1]

        return mac_address
    
    def scan_devices():
        """
        Getting Bluetooth Address of devices nearby.
        """
        try:
        # Run the hcitool scan command
            result = subprocess.run(['hcitool', 'scan'], capture_output=True, text=True, check=True)
            results = result.stdout.split('\n')[1:-1]
            devices = []
            for r in results:
                device = r.split('\t')[1:]
                devices.append({"bmac": device[0], "name": device[1]})
        
        except subprocess.CalledProcessError as e:
            print(f"Error running hcitool scan: {e}")
            print("Command output (if any):")
            print(e.output)
        
        return devices