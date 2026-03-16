import network
from time import sleep

class NoWifiError(Exception):
    pass

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wifi_creds = []
    
    with open(".wifi", "r") as f:
        wifi_creds.append(f.readline().strip())
        wifi_creds.append(f.readline().strip())
    
    wlan.connect(wifi_creds[0], wifi_creds[1])

    for _ in range(5):
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        print("waiting for connection")
        sleep(3)

    return wlan