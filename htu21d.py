import machine
import time

class HTU21D:
    def __init__(self, i2c, address=0x40):
        self.i2c=i2c
        self.address= address
    
    def read_temperature(self):
        self.i2c.writeto(self.address, b'\xf3')
        time.sleep (0.06)
        data= self.i2c.readfrom(self.address, 3)
        temp=(data[0] <<8 | data[1]) & 0xfffc
        return -46.85 + (175.72 * temp / 65536)
    
    def read_humidity(self):
        self.i2c.writeto(self.address, b'\xf5')
        time.sleep (0.06)
        data= self.i2c.readfrom(self.address, 3)
        hum=(data[0] <<8 | data[1]) & 0xfffc
        return -6 + (125.0 * hum / 65536)