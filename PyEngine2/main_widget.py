try:
    from PyEngine2.libs import *
    from PyEngine2.default_classes import *
    from PyEngine2.widgets import Menu
except ModuleNotFoundError:
    from libs import *
    from default_classes import *
    from widgets import Menu

# from PyEngine2.other_classes import *

class Window(OnClickDefaultWindowClass):

    def __init__(self, title = "New freaking project", winsize = "200x200+100+100", bg = "#ffffff", resizable = [True, True]):
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
        # self.__camera__ = __Camera__([0, 0], winsize)
        self.__object__ = self.__window__


        self.__canvas__ = BaseLibrary.Canvas(bg = bg)

    def clear(self): self.__canvas__.delete("all")

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
        if obj.__classinfo__() == "DefaultCanvasObject":
            if obj.__class__ == Rectangle:
                obj.__canvas_obj__ =  self.__canvas__.create_polygon(obj.__coords__, fill = obj.bg, width = obj.border, outline = obj.outline)

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

            elif obj.__class__ == Circle:
                obj.__canvas_obj__ = self.__canvas__.create_oval(obj.__coords__, fill = obj.bg, width = obj.border, outline = obj.outline)

        elif obj.__classinfo__() == "DefaultWindowObject":

            if obj.__class__ == Menu:
                self.__window__.config(menu = obj.__object__)

            elif obj.coords.__len__() == 2:
                if obj.mode == "px":
                    obj.__object__.place(x = obj.coords[0], y = obj.coords[1])
                elif obj.mode == "%":
                    obj.__object__.place(relx = obj.coords[0], rely = obj.coords[1])

            elif obj.coords.__len__() == 4:
                if obj.mode == "px":
                    obj.__object__.place(x = obj.coords[0], y = obj.coords[1], width = obj.coords[2], height = obj.coords[3])
                elif obj.mode == "%":
                    obj.__object__.place(relx = obj.coords[0], rely = obj.coords[1], relwidth = obj.coords[2], relheight = obj.coords[3])

        else: raise CantDrawWrongFormatError(obj)

    def wait(self, time, func): self.__window__.after(time, func)

    def key_game(self, key, func):
        if self.__window__.focus_get() != None and keyboard.is_pressed(key):
            func()

    def key_text(self, key, func): self.__window__.bind(key, func)

    # def cameraMove(self, step, vector):
    #     # WIP
    #     self.__camera__.move(step, vector, self.__objectList__)

    # def set_camera_position(self, position): self.__camera__.set_position(position, self.__objectList__)
