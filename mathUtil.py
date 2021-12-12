import math

def Clamp(num, min, max):
    if num < min:
        num = min
    elif num > max:
        num = max
    return num

