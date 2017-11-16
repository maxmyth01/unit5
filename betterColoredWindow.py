#Max Low
#11-16-17
#betterColoredWindow.py

#Max Low
#10-16-17
#colorChangeWindow.py -- every click changes the color

from ggame import *
from random import randint


color = [Color(0x0000FF,1),Color(0xFFFF00,1),Color(0x00FF00,1),Color(0xff0000,1)]
blueOutline = LineStyle(5,color[0])




def mouseClick(event):
    Rectangle = RectangleAsset(200,100,blueOutline,color[randint(0,3)])

    Sprite(Rectangle,(75,100))


App().listenMouseEvent('click', mouseClick)
App().run()
