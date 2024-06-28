import network

##############################
# __        _____ _____ ___ 
# \ \      / /_ _|  ___|_ _|
#  \ \ /\ / / | || |_   | | 
#   \ V  V /  | ||  _|  | | 
#    \_/\_/  |___|_|   |___|
#                          
##############################


# This would initialize the wifi object 
def wifi_init():
    wlan = network.WLAN(network.STA_IF)
    wlan.ative(True)
    wlan.scan() # this would be printed on the serial 
    wlan.isconnected()

# For creation of an access point 
def create_ap(wifi_ssid, wifi_pass, cn):
    ap = network.WLAN(netowrk.STA_IF)
    ap.config(ssid=wifi_ssid)
    ap.config(max_clients=cn)
    ap.active()


# To connect to a given network ssid, with key as password
def do_connect(ssid, key):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, key)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
