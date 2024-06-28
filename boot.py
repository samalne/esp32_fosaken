from machine import Pin, PWM, UART, SoftI2C, SoftSPI
import time
import os, vfs

# Other python files 
import ssd1306
import wifi

# TOADD: start the on boot code

# init code to start loading the I2C for the screen, buttons
# buzzer pin, and extra native device programable pins

#   ___ _   _ ___ _____ 
# |_ _| \ | |_ _|_   _|
#  | ||  \| || |  | |  
#  | || |\  || |  | |  
# |___|_| \_|___| |_|  
                     

wifi_init()


# load the screen/welcoming, or logo for the oled display

# some simple audio melody to be played
# need to import audio code library but not sure due to large sizes

# options to chose the mode (desktop/hax gadget)

#  _                   _                        
# | |__   __ _ _ __ __| |_      ____ _ _ __ ___ 
# | '_ \ / _` | '__/ _` \ \ /\ / / _` | '__/ _ \
# | | | | (_| | | | (_| |\ V  V / (_| | | |  __/
# |_| |_|\__,_|_|  \__,_| \_/\_/ \__,_|_|  \___|
#   ___ _   _ ___ _____ 
# |_ _| \ | |_ _|_   _|
#  | ||  \| || |  | |  
#  | || |\  || |  | |  
# |___|_| \_|___| |_|  
 
# The led pin is 4 on the esp32 ai thinker board


    # # button init as input
    # button1 = Pin(4, Pin.INPUT)
    #
    # # debug led output
    # deb_led = Pin(2, Pin.OUT)
    #
    
    # # Buzzer pin out
    # buz_pin = Pin(2, Pin.OUT)
    # buzz = PWM(buz_pin, freq=2000, duty=20)
    # buzz.duty(0)
    #
    #

##################################
#      _      _                 
#   __| | ___| |__  _   _  __ _ 
#  / _` |/ _ \ '_ \| | | |/ _` |
# | (_| |  __/ |_) | |_| | (_| |
#  \__,_|\___|_.__/ \__,_|\__, |
#                         |___/ 
##################################

# PIN 4 debug LED (flash)
dbg_led = Pin(4, Pin.OUT)
dbg_led.value(1) # on testing 
