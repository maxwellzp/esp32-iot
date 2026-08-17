import dht
from machine import Pin


class DHT22Sensor:
    def __init__(self, pin):
        self.sensor = dht.DHT22(Pin(pin))

    def read(self):
        self.sensor.measure()

        return {
            "temperature": self.sensor.temperature(),
            "humidity": self.sensor.humidity(),
        }
