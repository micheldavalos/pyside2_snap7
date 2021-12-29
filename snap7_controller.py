import snap7
from snap7.util import get_int, get_string, get_bool, get_real
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


class Snap7:
    status = False

    def __init__(self, address, rack=0, slot=0):
        self.address = address
        self.rack = rack
        self.slot = slot

        self.client = snap7.client.Client()

    def connect(self):
        try:
            self.client.connect(self.address, self.rack, self.slot)
            logging.info("Connected")
            self.status = True
            return True
        except:
            logging.info("Connection fail")
            return False

