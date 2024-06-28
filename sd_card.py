import machine
import os, vfs
#  ____  ____   ____              _ 
# / ___||  _ \ / ___|__ _ _ __ __| |
# \___ \| | | | |   / _` | '__/ _` |
#  ___) | |_| | |__| (_| | | | (_| |
# |____/|____/ \____\__,_|_|  \__,_|


def init_sdcard():
    sd = machine.SDCard(slot=2)
    vfs.mount(sd, '/sd')
    os.listdir('/sd')
    vfs.unmount('/sd')
