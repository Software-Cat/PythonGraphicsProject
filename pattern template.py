from graphics import *
import random
import math

screen_w = 1000
screen_h = 500

win = GraphWin("Pattern", screen_w, screen_h)
win.setBackground("white")

def pause():
    while True:
        key = win.getKey()
        if key == "Return":
            break

def draw_shape(xPos, yPos, color=color_rgb(0, 0, 0)):
    shape = Circle(Point(xPos, yPos), 20)
    shape.setOutline("black")
    shape.setWidth(3)
    shape.setFill(color)
    shape.draw(win)

    """
    winRect = Rectangle(Point(0, 0), Point(screen_w, screen_h))
    winRect.setFill('white')
    winRect.draw(win)
    """


xSpacing = 30
ySpacing = 30
xOffset = 0
yOffset = 10

themeRed = 50
themeGreen = 200
themeBlue = 100
colorVariation = 75

columns = math.ceil(screen_w / xSpacing)
rows = math.ceil(screen_h / ySpacing)

for row in range(rows):
    for column in range(columns):
        draw_shape(column*xSpacing+xOffset, row*ySpacing+yOffset, color_rgb(themeRed+random.randint(-int(colorVariation/2), int(colorVariation/2)), themeGreen+random.randint(-int(colorVariation/2), int(colorVariation/2)), themeBlue+random.randint(-int(colorVariation/2), int(colorVariation/2))))

pause()