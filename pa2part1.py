# a simple program to display a small rectangle
# in the middle of the window

from procgraphics import *
import procgraphics as pg


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




size(500,500)



drawOrange(50,100,60,55)
drawOrange(250,250,65,60)
drawOrange(186,164,70,65)
drawOrange(375,380,75,70)
drawOrange(160,300,80,75)
drawOrange(300,200,60,55)
drawOrange(430,267,65,60)
drawOrange(100,175,70,65)
drawOrange(40,360,75,70)
drawOrange(80,460,80,75)


text("CIS 2017 Cliff st. juste", 300,450)




#save the image as DrawnOrange.png
save("DrawnOrange.png")
