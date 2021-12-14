import os
from time import sleep

value = 0.00


def change_brightness():
    os.system(f"./kbrightness {value}")


while True:
    while value <= 1.00:
        value +=0.01
        change_brightness()
        sleep(0.001)
        if value == 0.99:
            break
    while value >= 0.00:
        value -=0.01
        change_brightness()
        sleep(0.001)
        if value == 0.01:
            break
