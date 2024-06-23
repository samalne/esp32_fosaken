from machine import Pin, PWM, UART, SoftI2C, SoftSPI
import time
import ssd1306
import network
import os, vfs

# TOADD: start the on boot code

# init code to start loading the I2C for the screen, buttons
# buzzer pin, and extra native device programable pins

#   ___ _   _ ___ _____ 
# |_ _| \ | |_ _|_   _|
#  | ||  \| || |  | |  
#  | || |\  || |  | |  
# |___|_| \_|___| |_|  
                     

# def init(): for the initialization of oled, buttons, buzzer, gpio as dependand
def init():
    # button init as input
    button1 = Pin(4, Pin.INPUT)

    # oled ssd1306 I2C init
    i2c = SoftI2C(sda=24, scl=22)
    button1.value(1) # this would light up indication that device is up
    display = ssd1306.SSD1306_I2C(32, 128, i2c)

    # displaying the booting message
    display.text('hello world device is powering up', 0, 0, 0)
    display.show()

    # Buzzer pin out
    buz_pin = Pin(2, Pin.OUT)
    buzz = PWM(buz_pin, freq=2000, duty=20)
    buzz.duty(0)

# __        _____ _____ ___ 
# \ \      / /_ _|  ___|_ _|
#  \ \ /\ / / | || |_   | | 
#   \ V  V /  | ||  _|  | | 
#    \_/\_/  |___|_|   |___|
                          


# This would initialize the wifi object 
def wifi_config():
    wlan = network.WLAN(netowrk.STA_IF)
    wlan.ative(True)
    wlan.scan()
    wlan.isconnected()
    # wlan.connect('ssid', 'pass')
    # wlan.config('mac')
    # wlan.ifconfig()

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

#  _        _    _   _ 
# | |      / \  | \ | |
# | |     / _ \ |  \| |
# | |___ / ___ \| |\  |
# |_____/_/   \_\_| \_|
   
## This is for future implementation ex: SPI ethernet controller
# def lan_config():
#     lan = network.LAN(mdc=PIN_MDC,  )
#     lan.active()
#     lan.ifconfig()
# load the screen/welcoming, or logo for the oled display

# some simple audio melody to be played
# need to import audio code library but not sure due to large sizes

#  ____  ____   ____              _ 
# / ___||  _ \ / ___|__ _ _ __ __| |
# \___ \| | | | |   / _` | '__/ _` |
#  ___) | |_| | |__| (_| | | | (_| |
# |____/|____/ \____\__,_|_|  \__,_|


# def init_sdcard():
#     sd = machine.SDCard(slot=2)
#     vfs.mount(sd, '/sd')
#     os.listdir('/sd')
#     vfs.unmount('/sd')

# options to chose the mode (desktop/hax gadget)


