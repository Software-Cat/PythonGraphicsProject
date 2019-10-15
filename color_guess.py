# import all the required python libaries: graphics and random
from graphics import *
import random

# create the graphics window and set background colour
win = GraphWin("Colour Guessing Game", 1000, 500)
win.setBackground('#232323')

# create a title for your game
titleBg = Rectangle(Point(0, 0), Point(1000, 135))
titleBg.setOutline('steelblue')
titleBg.setFill('steelblue')
titleBg.draw(win)
title = Text(Point(500, 67.5),"RGB Colour Guessing Game")
title.setTextColor('white')
title.setSize(48)
title.setFace('times roman')
title.draw(win)

colors = []
correctChoice = int
# generate random colors and questions
def randomise_answers():
    global colors
    global correctChoice

    colors = []
    for i in range(4):
        rand_r = random.randint(0, 255)
        rand_g = random.randint(0, 255)
        rand_b = random.randint(0, 255)
        colors.append([rand_r, rand_g, rand_b])
    correctChoice = random.randint(0, 3)
randomise_answers()

squares = []
# create 4 squares of random colour evenly spaced across the page
def create_squares(x, y, sideLen, spacing):
    global squares
    squares = []

    for i in range(4):
        # create a square (Rectangle) that is positioned based on the current 'i' value
        square = Rectangle(Point(x+i*sideLen+i*spacing, y), Point(x+(i+1)*sideLen+i*spacing, y+sideLen))
        # set the fill of the square to the random values of r,g and b
        square.setFill(color_rgb(colors[i][0], colors[i][1], colors[i][2]))
        # draw the square in the window
        square.draw(win)
        squares.append(square)

create_squares(225, 325, 100, 50)

def wait_for_click():
    while True:
        # get the click position of the mouse
        mousePos = win.getMouse()
        mouseX = mousePos.getX()
        mouseY = mousePos.getY()

        # check if the mouse clicked on the correct square, if it did display correct otherwise incorrect
        for i in range(4):
            currentSquare = squares[i]
            currentX1 = currentSquare.getP1().getX()
            currentY1 = currentSquare.getP1().getY()
            currentX2 = currentSquare.getP2().getX()
            currentY2 = currentSquare.getP2().getY()
            if mouseX > currentX1 and mouseX < currentX2 and mouseY > currentY1 and mouseY < currentY2:
                return i


''' main game '''
gameover = False

# create a rectangle that fills the whole screen
bgRect = Rectangle(Point(0, 0), Point(1000, 500))

# create a Text box that will display the results of the guess (correct/incorrect)
resultText = Text(Point(500, 125),"")
resultText.setSize(128)
resultText.setFill('white')

# create a Text box that will display the rgb of the correct choice
questionText = Text(Point(500, 225), f"rgb({colors[correctChoice][0]}, {colors[correctChoice][1]}, {colors[correctChoice][2]})")
questionText.setFill('white')
questionText.setSize(25)
questionText.setStyle('bold')
questionText.draw(win)

# create a Text box that will display the score of the player
score = 0
scoreText = Text(Point(500, 155), f"SCORE: {score}")
scoreText.setFill('white')
scoreText.setSize(12)
scoreText.draw(win)

while gameover == False:
    square_clicked = wait_for_click()

    if square_clicked == correctChoice:
        score += 1
        scoreText.setText(f"SCORE: {score}")
        randomise_answers()
        create_squares(225, 325, 100, 50)
        questionText.setText(f"rgb({colors[correctChoice][0]}, {colors[correctChoice][1]}, {colors[correctChoice][2]})")
    else:
        bgRect.setFill(color_rgb(colors[square_clicked][0], colors[square_clicked][1], colors[square_clicked][2]))
        bgRect.draw(win)
        resultText.setText("TOO BAD")
        resultText.draw(win)
        scoreText.setSize(24)
        scoreText.anchor = Point(500, 350)
        scoreText.undraw()
        scoreText.draw(win)
        gameover = True

# wait for click to close window
win.getMouse()
