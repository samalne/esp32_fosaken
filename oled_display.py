from machine import SoftI2C
import ssd1306

###################################
#  ____                           
# / ___|  ___ _ __ ___  ___ _ __  
# \___ \ / __| '__/ _ \/ _ \ '_ \ 
#  ___) | (__| | |  __/  __/ | | |
# |____/ \___|_|  \___|\___|_| |_|
###################################
  

# oled ssd1306 I2C init

def init_display(i2c_signal_data_pin, i2c_signal_clock_pin, x, y):
    # Declare i2c interface
    i2c = SoftI2C(sda=i2c_signal_data_pin, scl=i2c_signal_clock_pin)
    display = ssd1306.SSD1306_I2C( x, y, i2c)

    # displaying the booting message
    display.text('hello world device is powering up', 0, 0, 0)
    display.show()
    
    # TODO: Clear the display
    # display.fill(0)
    # display.show()
