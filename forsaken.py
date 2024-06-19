from machine import Pin, PWM, SoftI2C
import time
import ssd1306

# TOADD: start the on boot code

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


# init code to start loading the I2C for the screen, buttons
# buzzer pin, and extra native device programable pins
 
# def init(): for the initialization of oled, buttons, buzzer, gpio as dependand

# load the screen/welcoming, or logo for the oled display

# some simple audio melody to be played
# maybe some audio decoding

# options to chose the mode (desktop/hax gadget)

# connect / hak into a wifi (require a hacking module/wifi manager)
# Wifi manager

# sd card implementation
