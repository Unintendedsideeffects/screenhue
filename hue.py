import phue
import pprint
import discoverhue
from phue import Group
from screenhue import screenhue

username = 'fBrPrTmCruTvuPdF5sTBygT1kfpMSTsNpbiHGmi7'
brightness = 255
saturation = 254

def connect():
    # found = discoverhue.find_bridges()

    # bridgeIP.lower()
    # bridgeIP = bridgeIP.replace(':80', '')
    # bridgeIP = bridgeIP.replace('http://', '')
    # bridgeIP = bridgeIP.replace('/', '')
    
    bridge = phue.Bridge('192.168.86.21', username)
    bridge.connect()
    return bridge


def listLightsNames(bridge):
    return bridge.get_light_objects(bridge)
def pickLight():
    i = 1
    for light in lights:
        print("{}{}{}".format(i, ' ', light.name))
        i += 1
    choice = int(input('Write the number of the light you want '))
    return lights[choice]
     

bridge = connect()
lights = bridge.lights

lights[0].on = True
lights[0].brightness = brightness
lights[0].saturation = saturation
lights[0].hue = screenhue()






