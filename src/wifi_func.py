import network
from time import sleep


class NoWifiError(Exception):
    pass


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wifi_creds = []
    sleep(1)

    with open(".wifi", "r") as f:
        for line in f:
            wifi_creds.append(line.strip())

    for i in range(5):
        print("connection attempt:", i + 1)
        wlan.connect(wifi_creds[0], wifi_creds[1])
        sleep(3)

        if wlan.status() == 3:
            break
        elif wlan.status() == 1:
            print("connecting")

    if wlan.status() != 3:
        raise NoWifiError

    print("connected")
    print("IP: ", wlan.ifconfig()[0])
    return wlan
