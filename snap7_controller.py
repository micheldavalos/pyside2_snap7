import snap7
import snap7.util as s7
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

    def read_plc_string(self, db, offset, size):
        data = self.client.db_read(db, offset, size)
        s = s7.get_string(data, 0, size)
        # logging.info(s)
        return s

    def read_plc_int(self, db, offset, size):
        data = self.client.db_read(db, offset, size)
        value = s7.get_int(data, 0)
        # print(contador)
        # logging.info(contador)
        return value