try:
    from PyEngine2.libs import BaseLibrary, math
    from PyEngine2.default_classes import DEFAULT, DefaultCanvasObject
except ModuleNotFoundError:
    from libs import BaseLibrary, math
    from default_classes import DEFAULT, DefaultCanvasObject
    
class Sprite(DefaultCanvasObject):

    def __init__(self, win, directory, coords = [100, 100]):

        self.coords = coords
        self.directory = directory
        self.__image__ = BaseLibrary.PhotoImage(file = self.directory)
        self.__coords__ = [self.coords[0], self.coords[1], 0, 0]
        self.__coords__ = [self.__coords__[0], self.__coords__[1], self.__coords__[0]+self.__image__.width(), self.__coords__[1]+self.__image__.height()]
        win.__objectList__.append(self)
        self.__win__ = win

    def value_change(self, directory = DEFAULT, coords = DEFAULT):

        if directory == DEFAULT:
            directory = self.directory
        if coords == DEFAULT:
            coords = self.coords

        self.__init__(directory, coords)

    def zoom(self, times = int(1)):
        self.__image__ = self.__image__.zoom(times)
        self.__coords__ = [self.__coords__[0], self.__coords__[1], self.__coords__[0]+self.__image__.width(), self.__coords__[1]+self.__image__.height()]



class Rectangle(DefaultCanvasObject):

    def __init__(self, win, mode = "xywh", coords = [10, 10, 50, 70], bg = "#ffffff", border = 0, outline = "#000000", angle = 0):
        self.mode = mode
        self.angle = angle
        self.coords = coords
        self.bg = bg
        self.border = border
        self.outline = outline
        self.__coords__ = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.__canvas__ = BaseLibrary.Canvas()

        if mode == "xy2":
            self.__coords__ = coords
        elif mode == "xywh":
            x1 = coords[0]
            x2 = coords[2]+coords[0]
            y1 = coords[1]
            y2 = coords[1]+coords[3]
            self.__coords__ = [[x2, y1], [x1, y1], [x1, y2], [x2, y2]]
        else:
            raise WrongModeError(f"{self}, use 'xy2' or 'xywh' mode")
        if self not in win.__objectList__:
            win.__objectList__.append(self)

        self.center = [(self.__coords__[1][0]+self.__coords__[3][0])/2, (self.__coords__[1][1]+self.__coords__[3][1])/2]

        self.__coords__ = self.rotate(self.__coords__, self.angle, self.center)

        self.__win__ = win

    def rotate(self, points, angle, center):
        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = center
        new_points = []
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
        return new_points



class OvalSector(DefaultCanvasObject):
    def __init__(self, win, mode = "xywh", coords = [50, 50, 100, 100], angle = 45, start_angle = 0, bg = "white", border = 1, outline = "black"):
        self.mode = mode
        self.coords = coords
        self.angle = angle
        self.start_angle = start_angle
        self.bg = bg
        self.border = border
        self.outline = outline

        if mode == "xy2":
            self.__coords__ = coords
        elif mode == "xywh":
            self.__coords__ = [coords[0], coords[1], coords[2]+coords[0], coords[1]+coords[3]]
        else:
            raise WrongModeError(f"{self}, use 'xy2' or 'xywh' mode")
        if self not in win.__objectList__:
            win.__objectList__.append(self)
        self.__win__ = win


    def value_change(self, mode = DEFAULT, coords = DEFAULT, angle = DEFAULT, start_angle = DEFAULT, bg = DEFAULT, border = DEFAULT, outline = DEFAULT):
        if mode == DEFAULT:
            mode = self.mode
        if coords == DEFAULT:
            coords = self.coords
        if angle == DEFAULT:
            angle = self.angle
        if start_angle == DEFAULT:
            start_angle = self.start_angle
        if bg == DEFAULT:
            bg = self.bg
        if border == DEFAULT:
            border = self.border
        if outline == DEFAULT:
            outline = self.outline

        self.__init__(mode, coords, angle, start_angle, bg, border, outline)



class OvalSegment(DefaultCanvasObject):
    def __init__(self, win, mode = "xywh", coords = [50, 50, 100, 100], angle = 45, start_angle = 0, bg = "white", border = 1, outline = "black"):
        self.mode = mode
        self.coords = coords
        self.angle = angle
        self.start_angle = start_angle
        self.bg = bg
        self.border = border
        self.outline = outline

        if mode == "xy2":
            self.__coords__ = coords
        elif mode == "xywh":
            self.__coords__ = [coords[0], coords[1], coords[2]+coords[0], coords[1]+coords[3]]
        else:
            raise WrongModeError(f"{self}, use 'xy2' or 'xywh' mode")
        if self not in win.__objectList__:
            win.__objectList__.append(self)
        self.__win__ = win


    def value_change(self, mode = DEFAULT, coords = DEFAULT, angle = DEFAULT, start_angle = DEFAULT, bg = DEFAULT, border = DEFAULT, outline = DEFAULT):
        if mode == DEFAULT:
            mode = self.mode
        if coords == DEFAULT:
            coords = self.coords
        if angle == DEFAULT:
            angle = self.angle
        if start_angle == DEFAULT:
            start_angle = self.start_angle
        if bg == DEFAULT:
            bg = self.bg
        if border == DEFAULT:
            border = self.border
        if outline == DEFAULT:
            outline = self.outline

        self.__init__(mode, coords, angle, start_angle, bg, border, outline)



class Arc(DefaultCanvasObject):
    def __init__(self, win, mode = "xywh", coords = [50, 50, 100, 100], angle = 45, start_angle = 0, color = "white", border = 1):
        self.mode = mode
        self.angle = angle
        self.coords = coords
        self.start_angle = start_angle
        self.color = color
        self.border = border

        if mode == "xy2":
            self.__coords__ = coords
        elif mode == "xywh":
            self.__coords__ = [coords[0], coords[1], coords[2]+coords[0], coords[1]+coords[3]]
        else:
            raise WrongModeError(f"{self}, use 'xy2' or 'xywh' mode")
        if self not in win.__objectList__:
            win.__objectList__.append(self)
        self.__win__ = win


    def value_change(self, mode = DEFAULT, coords = DEFAULT, angle = DEFAULT, start_angle = DEFAULT, color = DEFAULT, border = DEFAULT):
        if mode == DEFAULT:
            mode = self.mode
        if coords == DEFAULT:
            coords = self.coords
        if angle == DEFAULT:
            angle = self.angle
        if start_angle == DEFAULT:
            start_angle = self.start_angle
        if color == DEFAULT:
            color = self.color
        if border == DEFAULT:
            border = self.border

        self.__init__(mode, coords, angle, start_angle, color, border)



class Line(DefaultCanvasObject):
    def __init__(self, win, coords = [10, 10, 100, 100], border = 0, color = "#000000"):
        self.coords = coords
        self.border = border
        self.color = color
        self.__coords__ = coords
        self.mode = "xy2"
        if self not in win.__objectList__:
            win.__objectList__.append(self)
        self.__win__ = win

    def value_change(self, coords = DEFAULT, border = DEFAULT, color = DEFAULT):
        if coords == DEFAULT:
            coords = self.coords
        if border == DEFAULT:
            border = self.border
        if color == DEFAULT:
            color = self.color

        self.__init__(self.__win__, coords, border, color)



class Oval(DefaultCanvasObject):
    def __init__(self, win, mode = "xywh", coords = [10, 10, 50, 70], bg = "#ffffff", border = 0, outline = "#000000"):
        self.mode = mode
        self.coords = coords
        self.bg = bg
        self.border = border
        self.outline = outline
        self.__coords__ = coords

        if mode == "xy2":
            self.__coords__ = coords
        elif mode == "xywh":
            self.__coords__ = [coords[0], coords[1], coords[2]+coords[0], coords[1]+coords[3]]
        else:
            raise WrongModeError(f"{self}, use 'xy2' or 'xywh' mode")
        if self not in win.__objectList__:
            win.__objectList__.append(self)
        self.__win__ = win



class Circle(DefaultCanvasObject):

    def __init__(self, win, coords = [100, 100], radius = 100, bg = "white", border = 0, outline = "black"):

        self.__coords__ = [coords[0]-radius, coords[1]-radius, coords[0]+radius, coords[1]+radius]
        self.coords = coords
        self.radius = radius
        self.bg = bg
        self.border = border
        self.outline = outline
        self.__win__ = win
        self.angle = 0
        if self not in win.__objectList__:
            win.__objectList__.append(self)
        
    def value_change(self, win = DEFAULT, coords = DEFAULT, radius = DEFAULT, bg = DEFAULT, border = DEFAULT, outline = DEFAULT, angle = 0):

        if radius == DEFAULT:
            radius = self.radius
        if coords == DEFAULT:
            coords = self.coords
        if bg == DEFAULT:
            bg = self.bg
        if border == DEFAULT:
            border = self.border
        if outline == DEFAULT:
            outline = self.outline

        self.__init__(self.__win__, coords, radius, bg, border, outline)

    def set_position(self, coords): self.value_change(coords = coords)


class Polygon(DefaultCanvasObject):

    def __init__(self, win, coords = [10, 20, 50, 100, 150, 30, 200, 200], bg = "#ffffff", border = 1, outline = "#000000"):

        self.coords = coords
        self.angle = 0
        self.bg = bg
        self.border = border
        self.outline = outline
        self.__coords__ = coords
        if self not in win.__objectList__:
            win.__objectList__.append(self)
        self.__win__ = win

    def value_change(self, coords = DEFAULT, bg = DEFAULT, border = DEFAULT, outline = DEFAULT):

        if coords == DEFAULT:
            coords = self.coords
        if bg == DEFAULT:
            bg = self.bg
        if border == DEFAULT:
            border = self.border
        if outline == DEFAULT:
            outline = self.outline

        self.__init__(self.__win__, coords, bg, border, outline)
