import pyscreenshot as ImageGrab #this is because pyscreenshot works on all OSs while ImageGrab is windows OSX only
import pprint
from converter import RGBtoXY


def screenhue():
    image = ImageGrab.grab()

    #image.save('screenshot.png')
    imX, imY = image.size
    colors = image.getcolors(imX * imY)

    comparePoint = colors[0]
    for count, color in colors:
        if count > comparePoint[0]:
            comparePoint = (count, color)

    comparePoint = comparePoint[1]
    red = comparePoint[0]
    green = comparePoint[1]
    blue = comparePoint[2]

    return RGBtoXY(red, green, blue)



    



