# coding: utf-8
#Programming Assignment 3
#Cliff St. Juste
#CIS 2017

#Project 3: Loops
import procgraphics as pg
from procgraphics import *



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







def draw():
    return

def setup():
    size(600,600)
    x1 = 80
    x2 = 600



    stepSize = 40

    numSteps = 10
    stepSize = (x2 - x1)//numSteps


    print("printing interpolation from",
          x1, "to",x2)
    interp = list(range(x1,x2,stepSize))
    interp.append(x2)
    for i in interp:
        print(i)
        drawOrange(i,44,10,10)
        drawOrange(44,i,30,30)
        drawOrange(i,i,20,20)
    print("done printing")
    text("CIS 2017 Cliff St.juste", 600,600)# NAme isn't shown for some reason





def lineShape(beginX, beginY, endX, endY):
    # build your lists
    numSteps = 10
    stepSizeX =(endX - beginX)//numSteps
    stepSizeY =(endY - beginY)//numSteps
    interpX = list(range(beginX,endX,stepSizeX))
    interpY = list(range(beginY,endY,stepSizeY))

    drawOrange(beginX, beginY, 40,40)


    for i in range (len(interpX)):
        drawOrange(interpX[i],interpY[i],40,40,)


    drawOrange(endX, endY, 40,40)


    #for i in len(interpY):
    #    drawOrange(interpY[i],interpX[i],40,40)


def nShapes(beginX, beginY, n):

    drawOrange(beginX, beginY, 20,20)
    for i in range (len(interpX)):
        drawOrange(random.randrange(pg.width,random.randrange(pg.height),40, 40))


def mousePressed():
    global k
    if k == "line":
        lineShape(pg.mouseX,pg.mouseY,30,30)
    else:
        nShapes(pg.mouseX,pg.mouseY , 5)

def keyPressed():
    global count
    global k

    if pg.key == 'b':
        fill('black')
    elif pg.key == 'y':
        fill('yellow')
    elif pg.key == 'p':
        fill('purple')
    elif pg.key == 's':
        count = count + 1
        filename = "drawing" + str(count) + ".png"
        save(filename)
    elif pg.key == 'q':
        quit()
    elif pg.key == "l":
        k = "line"
    else:
        fill('orange')

    fill('black')



runLoop(setup,draw,mousePressedFunc=mousePressed,keyPressedFunc=keyPressed)
