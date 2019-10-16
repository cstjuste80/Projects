# a simple program to display a small rectangle
# in the middle of the window

from procgraphics import *

def main():
    windowwidth = 500 # the width of the window
    windowheight = 500 # the height of the window
    size(windowwidth,windowheight) # create the window
    fill('black') # set the fill
    rect(windowwidth/2 -10, windowheight/2 -10, 20,20) # draw in center
    text("press enter in your shell to close", 50,30)
    input('press enter')


if __name__ == "__main__":
    main() # run the program.
