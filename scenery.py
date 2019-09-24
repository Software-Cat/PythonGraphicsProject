from graphics import *

screen_w = 1000
screen_h = 500

win = GraphWin("Pattern", screen_w, screen_h)
win.setBackground("skyblue")


def pause():
    while True:
        key = win.getKey()
        if key == "Return":
            break


pause()
