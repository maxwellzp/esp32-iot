import time
import gc


class SystemInfo:
    def __init__(self, wifi):
        self.wifi = wifi
        self.start_time = time.time()

    def get(self):
        gc.collect()

        return {
            "uptime": time.time() - self.start_time,
            "free_memory": gc.mem_free(),
            "wifi": {
                "ip": self.wifi.ip_address(),
                "rssi": self.wifi.rssi(),
            },
        }
