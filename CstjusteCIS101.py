# a simple program to display a small rectangle
# in the middle of the window

from procgraphics import *

def main():
    windowwidth = 500 # the width of the window
    windowheight = 500 # the height of the window
    size(windowwidth,windowheight) # create the window
    fill('yellow') # set the fill
    rect(0 ,0, 500,500) # draw in center
    fill('white')
    ellipse(160,150, 160,160)
    fill('blue')
    ellipse(180, 150, 60, 60)
    fill('black')
    ellipse(190,150,30,30)
    fill('white')
    ellipse(320,150,160,160)
    fill('blue')
    ellipse(300,150,60,60)
    fill('black')
    ellipse(290,150,30,30)
    fill('gold')
    ellipse(100,80, 20,20)
    fill('gold')
    ellipse(50,50,30,30)
    fill('gold')
    ellipse(250,390,25,25)
    fill('gold')
    ellipse(400,400,30,30)
    fill('gold')
    ellipse(350,350,20,20)
    fill('gold')
    ellipse(250,400,25,25)
    fill('gold')
    ellipse(390,500,40,40)
    fill('gold')
    ellipse(400,110,20,20)
    fill('gold')
    ellipse(250,400,30,30)
    fill('gold')
    ellipse(420,420,50,50)
    fill('gold')
    ellipse(20,410,40,40)
    fill('gold')
    ellipse(50,270,40,40)
    fill('gold')
    ellipse(480,70,30,30)
    fill('gold')
    ellipse(480,189,40,40)
    fill('gold')
    arc(250,250,100,50)
    arc(250,250,100,50)
    fill('gold')
    ellipse(240,240,50,100)
    fill('gold')
    ellipse(250,300,250,0)
    fill('white')
    rect(260,300,50,60)
    rect(170,300,50,60)
    fill('white')
    line(160,0,0,0)
    fill('black')
    ellipse(160,44,5,50)
    ellipse(190,49,5,50)
    ellipse(130,49,5,50)
    ellipse(300,49,5,50)
    ellipse(330,44,5,50)
    ellipse(360,50,5,50)
    fill('red')
    ellipse(100,300,5,5)
    ellipse(95,290,5,5)
    ellipse(85,300,5,5)
    ellipse(405,300,5,5)
    ellipse(400,290,5,5)
    ellipse(395,300,5,5)
    noStroke()
    fill('black')
    quad(1,1,1,1,1,1,1,1)
    beginShape(POLYGON)
    endShape
    fill('black')


    text("CIS 101 Fall 2017 Cliff St. Juste", 250,470)
    input('press enter')



if __name__ == "__main__":
    main() # run the program.
