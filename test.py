from graphics import *


def main():
    win = GraphWin("My Circle", 1000, 1000)

    blankImage = Image(320, 240)
    c = Circle(Point(160, 160), 10)
    c.draw(blankImage)


main()
