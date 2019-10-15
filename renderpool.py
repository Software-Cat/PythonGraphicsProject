from graphics import *


class RenderPool:

    DEFAULT_CONFIG = {
        "fill": 'white',
        "outline": "black",
        "width": "1",
        "arrow": "none",
        "text": "",
        "justify": "center",
        "font": ("helvetica", 12, "normal"),
        "tick": None
        # "tick": lambda self: pass
    }

    def __init__(self, tick=DEFAULT_CONFIG["tick"]):
        self.shapes = []
        if not tick is None:
            self.poolTick = tick
        renderPools.append(self)

    def draw(self, win):
        for shape in self.shapes:
            shape.draw(win)

    def undraw(self):
        for shape in self.shapes:
            shape.undraw()

    def clear(self):
        self.undraw()
        self.shapes = []

    def tick(self):
        if callable(getattr(self, "poolTick", None)):
            poolTick.tick(self)
        for shape in self.shapes:
            if callable(getattr(shape, "tick", None)):
                shape.tick(shape)

    def move(self, dx, dy):
        for shape in self.shapes:
            shape.move(dx, dy)

    def clone(self):
        newPool = RenderPool()
        newPool.shapes = self.shapes
        return newPool

    def getShapes(self):
        return self.shapes

    def getType(self, type):
        shapeList = []
        for shape in self.shapes:
            if isinstance(shape, type):
                shapeList.append(shape)
        return shapeList

    def point(self, x, y, fillCol=DEFAULT_CONFIG["fill"], strokeCol=DEFAULT_CONFIG["outline"], tick=DEFAULT_CONFIG["tick"]):
        point = Point(x, y)
        point.setFill(fillCol)
        point.setOutline(strokeCol)
        if not tick is None:
            point.tick = tick
        self.shapes.append(point)

    def line(self, x1, y1, x2, y2, fillCol=DEFAULT_CONFIG["fill"], strokeCol=DEFAULT_CONFIG["outline"], strokeWidth=DEFAULT_CONFIG["width"], arrow=DEFAULT_CONFIG["arrow"], tick=DEFAULT_CONFIG["tick"]):
        line = Line(Point(x1, y1), Point(x2, y2))
        line.setFill(fillCol)
        line.setOutline(strokeCol)
        line.setWidth(strokeWidth)
        line.setArrow(arrow)
        if not tick is None:
            line.tick = tick
        self.shapes.append(line)

    def cir(self, x, y, r, fillCol=DEFAULT_CONFIG["fill"], strokeCol=DEFAULT_CONFIG["outline"], strokeWidth=DEFAULT_CONFIG["width"], tick=DEFAULT_CONFIG["tick"]):
        circle = Circle(Point(x, y), r)
        circle.setFill(fillCol)
        circle.setOutline(strokeCol)
        circle.setWidth(strokeWidth)
        if not tick is None:
            circle.tick = tick
        self.shapes.append(circle)

    def rect(self, x1, y1, x2, y2, fillCol=DEFAULT_CONFIG["fill"], strokeCol=DEFAULT_CONFIG["outline"], strokeWidth=DEFAULT_CONFIG["width"], tick=DEFAULT_CONFIG["tick"]):
        rectangle = Rectangle(Point(x1, y1), Point(x2, y2))
        rectangle.setFill(fillCol)
        rectangle.setOutline(strokeCol)
        rectangle.setWidth(strokeWidth)
        if not tick is None:
            rectangle.tick = tick
        self.shapes.append(rectangle)

    def oval(self, x1, y1, x2, y2, fillCol=DEFAULT_CONFIG["fill"], strokeCol=DEFAULT_CONFIG["outline"], strokeWidth=DEFAULT_CONFIG["width"], tick=DEFAULT_CONFIG["tick"]):
        oval = Oval(Point(x1, y1), Point(x2, y2))
        oval.setFill(fillCol)
        oval.setOutline(strokeCol)
        oval.setWidth(strokeWidth)
        if not tick is None:
            oval.tick = tick
        self.shapes.append(oval)

    def poly(self, points, fillCol=DEFAULT_CONFIG["fill"], strokeCol=DEFAULT_CONFIG["outline"], strokeWidth=DEFAULT_CONFIG["width"], tick=DEFAULT_CONFIG["tick"]):
        points = [Point(*coordinates) for coordinates in points]
        polygon = Polygon(*points)
        polygon.setFill(fillCol)
        polygon.setOutline(strokeCol)
        polygon.setWidth(strokeWidth)
        if not tick is None:
            polygon.tick = tick
        self.shapes.append(polygon)

    def text(self, x, y, text=DEFAULT_CONFIG["text"], fillCol=DEFAULT_CONFIG["fill"], strokeCol=DEFAULT_CONFIG["outline"], font=DEFAULT_CONFIG["font"], tick=DEFAULT_CONFIG["tick"]):
        text = Text(Point(x, y), text)
        text.setFill(fillCol)
        text.setOutline(strokeCol)
        text.setFace(font[0])
        text.setSize(font[1])
        text.setStyle(font[2])
        if not tick is None:
            text.tick = tick
        self.shapes.append(text)

    def entry(self, x, y, width, text=DEFAULT_CONFIG["text"], fillCol=DEFAULT_CONFIG["fill"], font=DEFAULT_CONFIG["font"], tick=DEFAULT_CONFIG["tick"]):
        entry = Entry(Point(x, y), width)
        entry.setText(text)
        entry.setFill(fillCol)
        entry.setFace(font[0])
        entry.setSize(font[1])
        entry.setStyle(font[2])
        if not tick is None:
            entry.tick = tick
        self.shapes.append(entry)

    def image(self, x, y, filename, tick=DEFAULT_CONFIG["tick"]):
        image = Image(Point(x, y), filename)
        if not tick is None:
            image.tick = tick
        self.shapes.append(image)


renderPools = []


def mainloop(win, updateSpeed):
    for pool in renderPools:
        pool.draw(win)
    while True:
        for pool in renderPools:
            pool.tick()
            update(5)

def test():
    win = GraphWin()
    win.setCoords(0,0,10,10)

    pool = RenderPool()
    pool.text(5, 5, "Centered Text")
    pool.poly([[1, 1], [5, 3], [2, 7]])
    pool.entry(5, 6, 10)
    pool.draw(win)
    win.getMouse()
    userInput = pool.getType(Entry)[0].getText()
    pool.clear()

    pool.poly([[1, 1], [5, 3], [2, 7]], 'red', 'blue', 2)
    s = ""
    for pt in pool.getType(Polygon)[0].getPoints():
        s = s + "(%0.1f,%0.1f) " % (pt.getX(), pt.getY())
    pool.text(5, 5, userInput)
    pool.entry(5, 6, 10, "Spam!", "green", tick=lambda self:self.move(2, 0))
    pool.tick()
    pool.draw(win)
    win.getMouse()
    pool.clear()

    pool.poly([[1, 1], [5, 3], [2, 7]], 'red', 'blue', 2, lambda self:self.move(2, 3))
    pool.entry(5, 6, 10, "Spam!", "green", tick=lambda self:self.move(2, 0))
    pool.tick()
    s = ""
    for pt in pool.getType(Polygon)[0].getPoints():
        s = s + "(%0.1f,%0.1f) " % (pt.getX(), pt.getY())
    pool.text(5, 5, s)
    pool.draw(win)
    win.getMouse()
    pool.clear()

    pool.text(5, 5, s, font=("helvetica", 12, "bold"))
    pool.draw(win)
    win.getMouse()
    pool.clear()

    pool.text(5, 5, s, font=("helvetica", 12, "normal"))
    pool.draw(win)
    win.getMouse()
    pool.clear()

    pool.text(5, 5, s, font=("helvetica", 12, "italic"))
    pool.draw(win)
    win.getMouse()
    pool.clear()

    pool.text(5, 5, s, font=("helvetica", 12, "bold italic"))
    pool.draw(win)
    win.getMouse()
    pool.clear()

    pool.text(5, 5, s, font=("helvetica", 14, "bold italic"))
    pool.draw(win)
    win.getMouse()
    pool.clear()

    pool.text(5, 5, s, font=("arial", 20, "bold italic"))
    pool.draw(win)
    win.getMouse()
    pool.clear()

    win.close()

if __name__ == '__main__':
    test()