from machine import PWM, Pin
import time

#################################
#  ____                         
# | __ ) _   _ ___________ _ __ 
# |  _ \| | | |_  /_  / _ \ '__|
# | |_) | |_| |/ / / /  __/ |   
# |____/ \__,_/___/___\___|_|   
#
#################################
 
# Buzzer pin out

# function to do a number of beeps for a ms duration
def beep(pin, frequency, beeps, duration):
    buz_pin = Pin(pin, Pin.OUT)
    buzz = PWM(buz_pin, freq=2000, duty=0)
    buzz.freq(frequency)
    for i in range(beeps):
        buzz.duty(75)
        delay_ms(duration)
        buzz.duty(0)
        delay_ms(duration)
