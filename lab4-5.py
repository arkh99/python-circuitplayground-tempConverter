import time
from adafruit_circuitplayground import cp

def CelToFahr(F):
    C = (F - 32) * 5 / 9
    return C


loop = True
while loop:
    temp = cp.temperature
    if cp.button_a
        if cp.switch:
            print("Button A pressed!")
            cp.red_led = True

            print("The temp in fahr is ", CelToFahr(temp))
        else:
            print("The temp in C is ", temp)
    
        time.sleep(1)
    






