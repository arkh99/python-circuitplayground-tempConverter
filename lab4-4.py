import time
from adafruit_circuitplayground import cp



temp = cp.temperature
def CelToFahr(F):
    C = (F - 32) * 5 / 9
    return C

while True:
    if cp.switch:
        print("The temp in F is ", CelToFahr(temp))

    else:
        print("The temp in C is ", temp)
    
    time.sleep(1)

