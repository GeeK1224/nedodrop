"""
P2P (PEER2PEER) - Logic of the app.
"""

from config import File
import os
import tqdm
import socket
import random
import asyncio
import argparse
from bleak import BleakScanner
from loguru import logger

from utils import Utils
from config import DATA_SIZE, FILE, MESSAGE, END


logger.add("comm.log", format="{time:YYYY-MM-DD at HH:mm:ss}- {module} - {level} - {message}", level="DEBUG")

class BluetoothServices:
    """
    This class is responsible for bluetooth manipulation.
    """

    def __init__(self):
        self.bmac:str = Utils.get_bluetooth_mac_address()
        self.channel:int = 4 # random.randint(4, 10)
        self.sock = None # socket
        self.comm = None # communication
    
    async def find(self, args) -> list:
        """
        This asynchronous method returns dict of dicts of devices nearby.
        ```
        devices: list = asyncio.run(find(args))
        ```
        """
        logger.info("looking for devices...")

        devices = await BleakScanner.discover()

        return devices
    
    def bind(self) -> tuple:
        """
        This method responsible for starting bluetooth to make it visible
        """
        try:
            self.sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            self.sock.bind((self.bmac, self.channel))
            self.sock.listen(1)

            self.comm, addr =  self.sock.accept()
        except OSError as e:
            logger.error(e)

    def connect(self, bmac, channel):
        self.comm = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.comm.connect((bmac, channel))
        
    
    def send_info(self, host, port):
        """
        This method sending information we need to connect to HTTP socket,
        (host, port).
        """
        try:
            logger.info("sending message with host and port")
            self.comm.send(host.encode('utf-8'))
            self.comm.send(port.encode('utf-8'))

        except OSError as e:
            logger.error(e)
            self.close()
    
    def receive_info(self) -> tuple:
        """
        This method receiving information we need to connect to HTTP socket,
        (host, port).
        """
        try:
            logger.info("received message with host and port")
            host = self.comm.recv(DATA_SIZE)
            port = self.comm.recv(DATA_SIZE)
        
        except OSError as e:
            logger.error(e)
            self.close()
        
        return (host, port)
            
    
    def close(self):
        self.comm.close()
        self.sock.close()

class NedodropService:
    """
    This class responsible for HTTP manipulation and file transfer.
    """

    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 8000
        self.sock = None
        self.sender = None
        self.receiver = None

    def bind(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.host, self.port))
            self.sock.listen(5)

            self.sender, addr = self.sock.accept()

        except OSError as e:
            logger.error(e)

    def connect(self, host, port):
        self.receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receiver.connect((host, port))

    def send_message(self, msg):
        try:
            logger.info('sended message')
            self.sender.send(MESSAGE.encode('utf-8'))
            self.sender.send(msg.encode('utf-8'))
        
        except OSError as e:
            logger.error(e)
            self.close()

    def send_file(self, file_path):
        try:
            file = open(file_path, "rb")
            size = str(os.path.getsize(filename=file_path))
            logger.info("sending file name and size")
            self.sender.send(file_path.split('/')[-1].encode('utf-8'))
            self.sender.send(size.encode('utf-8'))

        except OSError as e:
            logger.error(e)
            self.close()

        data = file.read()
        self.sender.sendall(data)
        self.sender.send(END)

        file.close()
    
    def receive_file(self):
        try:
            logger.info("receiving file name and size")
            file = File()
            file.name = self.receiver.recv(DATA_SIZE).decode()
            file.size = int(self.receiver.recv(DATA_SIZE).decode())
            progress = tqdm.tqdm(unit='B', unit_scale=True, unit_divisor=1000, total=file.size)
            file_bytes = b""
            done = False
            while not done:
                data = self.receiver.recv(DATA_SIZE)
                if file_bytes[-5:] == END:
                    done = True
                else:
                    file_bytes += data
                progress.update(DATA_SIZE)

            file.create(file_bytes=file_bytes)

        except OSError as e:
            logger.error(e)
            
    
    def close(self):
        """
        This method for closing sock and comm.
        """
        try:
            self.receiver.close()
        except AttributeError:
            pass
        try:
            self.sender.close()
            self.sock.close()
        except AttributeError:
            pass


