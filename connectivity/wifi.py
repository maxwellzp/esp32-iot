import time
import network


class WiFi:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self, timeout=15):
        if self.wlan.isconnected():
            return True

        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)

        start = time.time()

        while not self.wlan.isconnected():
            if time.time() - start >= timeout:
                return False

            time.sleep(0.5)

        return True

    def ip_address(self):
        if not self.wlan.isconnected():
            return None

        return self.wlan.ifconfig()[0]

    def rssi(self):
        if not self.wlan.isconnected():
            return None

        return self.wlan.status("rssi")
