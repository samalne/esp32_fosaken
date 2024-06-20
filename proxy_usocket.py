import usocket
import _thread

#  ____  ____   _____  ____   __  ____  _   _ ___ _____ _____ _____ ____  
# |  _ \|  _ \ / _ \ \/ /\ \ / / / ___|| \ | |_ _|  ___|  ___| ____|  _ \ 
# | |_) | |_) | | | \  /  \ V /  \___ \|  \| || || |_  | |_  |  _| | |_) |
# |  __/|  _ <| |_| /  \   | |    ___) | |\  || ||  _| |  _| | |___|  _ < 
# |_|   |_| \_\\___/_/\_\  |_|   |____/|_| \_|___|_|   |_|   |_____|_| \_\
                                                                        



HEX_FILTER = ''.join(
    (len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src.decode()
    results = list()
    for i in range(0, len(src), length)