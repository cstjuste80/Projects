# coding: utf-8
import procgraphics as pg
from procgraphics import *


count= 0 # counter for saved files

def drawOrange(x,y,w,h):
    fill("orange")
    stroke("yellow")
    width = 45
    height = 90
    wRatio = w / width
    hRatio = h/ height
    strokeWeight(2 * wRatio)
    ellipse(x,y,w,h)

    fill("black")
    stroke("black")
    ellipse(x-w/4,y-h/5,w/10,h/10)


    fill("green")
    stroke("green")
    ellipse(x-w/4,y-h/2.5,w/12,h/3)




def setup():
    size(650,650)
    background("blue")
    fill("red")
    ellipse(pg.width/2,pg.height/2,300,300) # draw a red circle




def draw():
    # do nothing
    return


def mousePressed():
    drawOrange(pg.mouseX,pg.mouseY,10,10)

def keyPressed():
    global count

    if pg.key == 'b':
        drawOrange(pg.mouseX,pg.mouseY,30,30)
    elif pg.key == 'y':
        drawOrange(pg.mouseX,pg.mouseY,50,50)
    elif pg.key == 'p':
        drawOrange(pg.mouseX,pg.mouseY,70,70)
    elif pg.key == 's':
        count = count + 1
        filename = "drawing" + str(count) + ".png"
        save(filename)
    elif pg.key == 'q':
        quit()
    else:
        fill('orange')

runLoop(setup,draw,mousePressedFunc=mousePressed,keyPressedFunc=keyPressed)
