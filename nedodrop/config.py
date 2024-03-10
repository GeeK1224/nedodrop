from utils import Utils
from loguru import logger
import os
import random
import socket
import platform
import ssl
import subprocess
import json

logger.add("client.log", format="{time:YYYY-MM-DD at HH:mm:ss}- {module} - {level} - {message}", level="DEBUG")

DATA_SIZE = 1024
MESSAGE = b'<MSG>'
FILE = b'<FIL>'
END = b'<END>'
MACOS = 'darwin'
LINUX = 'linux'
WINDOWS = 'windows'
# operating_system = platform.system()
# In file entity I had class File and Peer process them.

class File:
    def __init__(self):
        pass


class NedodropConfig:
    """
    This class is used to create, read, update, delete configuration files. 
    """
    def __init__(self,
                 nedodrop_dir:str = "~/.nedodrop",
                 computer_model:str = None,
                 device_name:str = None,
                 server_host:str = None,
                 port:int = 8888,
                 bmac:str = None,
                 channel:int = 4,
                 name:str = None,
                 email:str = None,
                 phone:str = None,
                 social_media:dict = None
                 ):

        logger.debug("Initiate configs")
        self.nedodrop_dir = os.path.expanduser(nedodrop_dir)
        self.config_name:str = "config.json"
        self.port = port
        if device_name is None:
            device_name = "untitled"
        self.device_name = device_name
        if server_host is None:
            server_host = socket.gethostbyname(socket.gethostname())
        self.server_host = server_host
        if computer_model is None:
            computer_model = platform.system().lower()
        self.computer_model = computer_model
        if bmac is None:
            bmac = Utils.get_bluetooth_mac_address()
        self.bmac = bmac
        self.channel = channel
        self.name = name
        self.email = email
        self.phone = phone
        self.social_media = social_media

    def save_config(self):
        """
        This method responsible for creating configuration JSON file.
        """
        logger.info("Created config file")
        structure = {
            "user": {
                "name": self.name,
                "phone": self.phone,
                "email": self.email,
                "social_media": self.social_media,
            },
            "device": {
                "nedodrop_dir": self.nedodrop_dir,
                "config_name": self.config_name,
                "computer_model": self.computer_model,
                "device_name": self.device_name,
                "server_host": self.server_host,
                "port": self.port,
                "bmac": self.bmac,
                "channel": self.channel,
                },
        }

        data = json.dumps(structure, indent=2)
        with open(self.config_name, 'w+') as config:
            config.write(data)


    def load_config(self):
        """
        This method responsible for parsing configuration JSON file.
        """
        logger.info("Parsing config file")
        with open(self.config_name, 'r') as config:
            data = json.loads(config.read())

            self.name = data['user']['name']
            self.phone = data['user']['phone']
            self.email = data['user']['email']
            self.social_media = data['user']['social_media']

            self.nedodrop_dir = data['device']['nedodrop_dir']
            self.congif_name = data['device']['config_name']
            self.computer_model = data['device']['computer_model']
            self.device_name = data['device']['device_name']
            self.server_host = data['device']['server_host']
            self.port = data['device']['port']
            self.bmac = data['device']['bmac']
            self.channel = data['device']['channel']


    def update_config(self):
        with open(self.config_name) as config:
            pass

    def delete_config(self):
        logger.info("Config file deleted successfully")
        try:
            os.remove(os.getcwd() + "/" + self.config_name)
        except FileNotFoundError:
            logger.info("File not found")

    def __str__(self):
        return f"computer-model: {self.computer_model}\nname: {self.name}\nemail: {self.email}\nphone: {self.phone}\nsocial-media: {self.social_media}"