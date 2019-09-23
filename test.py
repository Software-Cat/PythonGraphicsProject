from graphics import *

def main():
    win = GraphWin("My Circle", 1000, 1000)

    c = Circle(Point(500,500), 200)
    c.setFill('blue')
    c.draw(win)

    r = Rectangle(Point(200, 200), Point(600, 600))
    r.setFill('red')
    r.draw(win)

main()