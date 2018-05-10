import math

def EnhanceColor(normalized):
    if normalized > 0.04045:
        return math.pow( (normalized + 0.055) / (1.0 + 0.055), 2.4)
    else:
        return normalized / 12.92

def RGBtoXY(r, g, b):
    rNorm = r / 255.0
    gNorm = g / 255.0
    bNorm = b / 255.0

    rFinal = EnhanceColor(rNorm)
    gFinal = EnhanceColor(gNorm)
    bFinal = EnhanceColor(bNorm)
    
    X = rFinal * 0.649926 + gFinal * 0.103455 + bFinal * 0.197109
    Y = rFinal * 0.234327 + gFinal * 0.743075 + bFinal * 0.022598
    Z = rFinal * 0.000000 + gFinal * 0.053077 + bFinal * 1.035763

    if X + Y + Z == 0:
        return (0,0)
    else:
        x = X / (X + Y + Z)
        y = Y / (X + Y + Z)
        
        # return (xFinal, yFinal)
        a = (x - 0.332)
        b = 0.1858 - y
        value = pow(437*(a/b), 3)
        value += pow(3601*(a/b), 2)
        value += 6831*(a/b)
        value += 5517

        value = (1/value * 10000000000)
        print(value)
        return value