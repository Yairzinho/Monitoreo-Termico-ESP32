import network
from secrets import WIFI_SSID, WIFI_PASS
import time

def conectar_wifi():
    wlan= network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectado a red...")
        wlan.connect(WIFI_SSID,WIFI_PASS)
        
        timeout=10
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -=1
            
    if wlan.isconnected():
        print("Conectado! IP:", wlan.ifconfig()[0])
        return True
    else:
        print(" Error de conexión")
        return False