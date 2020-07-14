import tkinter as BaseLibrary
import keyboard
import numpy as np

class DEFAULT():
    def __init__(self): self.default = "default"


def addPhysics(obj, gravity = 9.8, warnings_pass = False):

    if not(warnings_pass):
        if obj.__class__ not in physicsRecommendedClasses:
            print(f"Not recommended to use physics to {obj.__class__}")


    class Physics():

        def __init__(self, gravity = 9.8):
            self.fallTime = 1
            self.gravity = gravity
            self.verticalSpeed = 1.

        def update(self):
            self.verticalSpeed = self.verticalSpeed + self.gravity * self.fallTime /10000
            self.fallTime += 1

    obj.physics = Physics(gravity)
            

def collision(obj1, obj2):
    classes = [Rectangle, Oval]
    if obj1.__class__ in classes and obj2.__class__ in classes:

        if (obj1.__coords__[0] < obj2.__coords__[2] and
            obj1.__coords__[1] < obj2.__coords__[3] and 

            obj1.__coords__[2] > obj2.__coords__[0] and 
            obj1.__coords__[3] > obj2.__coords__[1]):

            return True

    return False


class DefaultCanvasObject():
            
    def move(self, step, vector = "x"):
        if self.__class__ in modeclasses:
            if vector == "y":

                if self.mode == "xywh":
                    self.value_change(coords = [self.coords[0], self.coords[1]+step, self.coords[2], self.coords[3]])

                elif self.mode == "xy2":
                    self.value_change(coords = [self.coords[0], self.coords[1]+step, self.coords[2], self.coords[3]+step])

                    
            elif vector == "x":

                if self.mode == "xywh":
                    self.value_change(coords = [self.coords[0]+step, self.coords[1], self.coords[2], self.coords[3]])

                elif self.mode == "xy2":
                    self.value_change(coords = [self.coords[0]+step, self.coords[1], self.coords[2]+step, self.coords[3]])
        
        else:
            outcoords = self.__coords__

            if vector == "x":
                for i in range(self.__coords__.__len__()):

                    if i % 2 == 0:
                        outcoords[i] += step
            
            elif vector == "y":
                for i in range(self.__coords__.__len__()):

                    if i % 2 == 1:
                        outcoords[i] += step

            self.value_change(coords = outcoords)

    def set_position(self, coords):
        global modeclasses

        outcoords = self.coords

        for i in range(self.__coords__.__len__()):
            if i in coords:
                outcoords[i] = coords[i]
            
        self.value_change(coords = outcoords)
        


    def value_change(self, mode = DEFAULT, coords = DEFAULT, bg = DEFAULT, border = DEFAULT, outline = DEFAULT):
        if mode == DEFAULT:
            mode = self.mode
        if coords == DEFAULT:
            coords = self.coords
        if bg == DEFAULT:
            bg = self.bg
        if border == DEFAULT:
            border = self.border
        if outline == DEFAULT:
            outline = self.outline
        # if angle == None:
        #     angle = self.__angle__

        self.__init__(self.__win__, mode, coords, bg, border, outline)

    def on_click(self, win, func, button = 1):

        win.__canvas__.tag_bind(self.__canvas_obj__, f"<Button-{button}>", lambda event: func())


class CantDrawWrongFormatError(Exception):
    def __init__(self, obj): pass


class WrongModeError(Exception):
    def __init__(self, obj): pass

#-------------------------------------------------------------------------------------------------------------------------------------------------------

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
    def __init__(self, win, mode = "xywh", coords = [10, 10, 50, 70], bg = "#ffffff", border = 0, outline = "#000000"):
        self.mode = mode
        self.coords = coords
        self.bg = bg
        self.border = border
        self.outline = outline
        self.__coords__ = [0, 0, 0, 0]
        self.__canvas__ = BaseLibrary.Canvas()

        if mode == "xy2":
            self.__coords__ = coords
        elif mode == "xywh":
            self.__coords__ = [coords[0], coords[1], coords[2]+coords[0], coords[1]+coords[3]]
        else:
            raise WrongModeError(f"{self}, use 'xy2' or 'xywh' mode")
        if self not in win.__objectList__:
            win.__objectList__.append(self)
        self.__win__ = win



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

        self.__init__(coords, border, color)



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



class Polygon(DefaultCanvasObject):

    def __init__(self, win, coords = [10, 20, 50, 100, 150, 30, 200, 200], bg = "#ffffff", border = 1, outline = "#000000"):

        self.coords = coords
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

        self.__init__(coords, bg, border, outline)

#-------------------------------------------------------------------------------------------------------------------------------------------------------

class Window():

    def __init__(self, title = "New freaking project", winsize = "200x200+100+100", bg = "#000000", resizable = [True, True]):
        self.__objectList__ = []
        self.bg = bg
        self.resizable = resizable
        self.winsize = winsize
        self.title = title
        self.__window__ = BaseLibrary.Tk()
        self.__window__.config(bg = bg)
        self.__window__.title(title)
        self.__window__.geometry(winsize)
        self.__window__.resizable(resizable[0], resizable[1])
        self.__camera__ = __Camera__([0, 0], winsize)


        self.__canvas__ = BaseLibrary.Canvas(bg = bg)

    def clear(self):
        self.__canvas__.delete("all")

    def end(self):
        self.__canvas__.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.__window__.mainloop()

    def tickFunction(self, func, tick = 20):
        tick1 = int(1/tick*1000)
        func()
        self.__window__.after(tick1, lambda: self.tickFunction(func, tick))

    def renderFunction(self, func, fps = 120):
        fps1 = int(1/fps*1000)
        func()
        self.__window__.after(fps1, lambda: self.renderFunction(func, fps))

    def drawObj(self, obj):
        if obj.__class__ == Rectangle:
            obj.__canvas_obj__ =  self.__canvas__.create_rectangle(obj.__coords__, fill = obj.bg, width = obj.border, outline = obj.outline)

        elif obj.__class__ == Oval:
            obj.__canvas_obj__ = self.__canvas__.create_oval(obj.__coords__, fill = obj.bg, width = obj.border, outline = obj.outline)

        elif obj.__class__ == Line:
            obj.__canvas_obj__ = self.__canvas__.create_line(obj.__coords__, width = obj.border, fill = obj.color)

        elif obj.__class__ == OvalSector:
            obj.__canvas_obj__ = self.__canvas__.create_arc(obj.__coords__, start = obj.start_angle, extent = obj.angle, fill = obj.bg, width = obj.border, outline = obj.outline)

        elif obj.__class__ == OvalSegment:
            obj.__canvas_obj__ = self.__canvas__.create_arc(obj.__coords__, style = BaseLibrary.CHORD, start = obj.start_angle, extent = obj.angle, fill = obj.bg, width = obj.border, outline = obj.outline)

        elif obj.__class__ == Arc:
            obj.__canvas_obj__ = self.__canvas__.create_arc(obj.__coords__, style = BaseLibrary.ARC, start = obj.start_angle, extent = obj.angle, outline = obj.color, width = obj.border)

        elif obj.__class__ == Polygon:
            obj.__canvas_obj__ = self.__canvas__.create_polygon(obj.__coords__, fill = obj.bg, width = obj.border, outline = obj.outline)

        elif obj.__class__ == Sprite:
            obj.__canvas_obj__ = self.__canvas__.create_image(obj.__coords__[0], obj.__coords__[1], image = obj.__image__)

        else:
            raise CantDrawWrongFormatError(obj)

    def wait(self, time, func):
        self.__window__.after(time, func)

    def key_game(self, key, func):
        if self.__window__.focus_get() != None and keyboard.is_pressed(key):
            func()

    def key_text(self, key, func):
        self.__window__.bind(key, func)

    def cameraMove(self, step, vector):
        # WIP
        self.__camera__.move(step, vector, self.__objectList__)

    def set_camera_position(self, position):
        self.__camera__.set_position(position, self.__objectList__)

class __Camera__():
    # Work in progress

    def __init__(self, coords = [0, 0], size = "200x200+100+100"):

        self.coords = coords
        sizeS = size.split("+")[0].split("x")

    def move(self, step, vector = "x", objList = []):

        if vector == "x":
            self.coords[0] += step
        elif vector == "y":
            self.coords[1] += step

        for obj in objList:
            obj.move(step, vector)

    def set_position(self, position, objList):


        for obj in objList:

            out = {}
            
            if hasattr(obj, "mode"):
                if obj.mode == "xywh":
                    coords = obj.coords[:2]
                elif obj.mode == "xy2":
                    coords = obj.coords
                for coord in coords:
                    if coords.index(coord) % 2 == 0:
                        out[coords.index(coord)] = position[0] - self.coords[0] + coord
                    elif coords.index(coord) % 2 == 1:
                        out[coords.index(coord)] = position[1] - self.coords[1] + coord
                    coords[coords.index(coord)] = None
            
            obj.set_position(out)
        self.coords = position
                

#-------------------------------------------------------------------------------------------------------------------------------------------------------

physicsRecommendedClasses = [Rectangle, Oval, Polygon, OvalSegment, OvalSector, Arc, Line]
modeclasses = [Rectangle, Oval, OvalSector, OvalSegment, Arc, Line]