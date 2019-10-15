from graphics import *
from renderpool import *


def pause():
    while True:
        key = win.getKey()
        if key == "Return":
            break


screenW = 1000
screenH = 500

win = GraphWin("Scenery", screenW, screenH, False)
win.setBackground("skyblue")

pool = RenderPool()
pool.poly([[0, 100], [100, 100], [100, 0], [0, 0]],
          tick=lambda self: self.move(10, 10))
pool.rect(100, 100, 200, 200)
pool.poolTick = lambda self: self.move(1, 1)


mainloop(win, 5)

pause()
