#Max Low
#11-21-17
#antsDemo.py -- how to maove many objects

from ggame import *
from random import randint

WIDTH = 900
HIGHT = 500
NUMANTS =50

#move each ant randomly in x and y
def step():
    dx = randint(-4,3)
    dy = randint(-4,3)
    if ant.x + dx > 0 and ant.x + dx < WIDTH:
        ant.x += dx
    if ant.y + dy > 0 and ant.y + dy < HIGHT:
        ant.y += dy
        
# creates te ants
if _name_ == '_main_':
    data = {}
    data[antList] = []

    red = Color(0xFF0000,1)
    ant = CircleAsset(20,LineStyle(1,red),red)

    #put each ant in the ant list
    for i in range(NUMANTS):
        data[antList].append(Sprite(ant,(randint(1,WIDTH),randint(1,HIGHT))))
        
App().run(step)
