from machine import Pin

##################################
#      _      _                 
#   __| | ___| |__  _   _  __ _ 
#  / _` |/ _ \ '_ \| | | |/ _` |
# | (_| |  __/ |_) | |_| | (_| |
#  \__,_|\___|_.__/ \__,_|\__, |
#                         |___/ 
##################################

# debug led output
deb_led = Pin(2, Pin.OUT)

# PIN 4 debug LED (flash)
dbg_led = Pin(4, Pin.OUT)
dbg_led.value(1) # on testing 
