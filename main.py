import time

from config import DHT22_PIN
from config_private import WIFI_SSID, WIFI_PASSWORD

from connectivity.wifi import WiFi
from sensors.dht22 import DHT22Sensor
from api.server import APIServer
from system.info import SystemInfo

wifi = WiFi(WIFI_SSID, WIFI_PASSWORD)

if not wifi.connect():
    print("Wi-Fi connection failed")
    raise RuntimeError("Unable to connect to Wi-Fi")

print("Wi-Fi connected")
print("IP address:", wifi.ip_address())


sensor = DHT22Sensor(DHT22_PIN)

system_info = SystemInfo(wifi)

server = APIServer(sensor, system_info)

server.start()
