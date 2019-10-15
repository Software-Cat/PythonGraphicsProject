# import all the required python libaries: graphics and random
from graphics import *
import random

# create the graphics window and set background colour
win = GraphWin("Colour Guessing Game", 1000, 500 )
win.setBackground("white")

# create a title for your game
title = Text(Point(500,100),"Bowen's Colour Guessing Game")
title.setTextColor('black')
title.setSize(48)
title.draw(win)

# generate a random number between 0 and 3


# create 4 squares of random colour evenly spaced across the page

for i in range(4):
    #generate random nums between 0 and 255 for red, green and blue values
    rand_r = random.randint(0, 255)
    rand_g = random.randint(0, 255)
    rand_b = random.randint(0, 255)

    # create a square (Rectangle) that is positioned based on the current 'i' value
    square = Rectangle(Point(0,0), Point(0,0))
    # set the fill of the square to the random values of r,g and b

    # draw the square in the window


''' main game '''
gameover = False

# create a Text box that will display the results of the guess (correct/incorrect)
resultText = Text(Point(500,250),"")
resultText.setSize(24)
resultText.draw(win)

while gameover == False:
    # get the click position of the mouse
    

    # check if the mouse clicked on the correct square, if it did display correct otherwise incorrect



    # exit game when game is over
    gameover = True
    
    


