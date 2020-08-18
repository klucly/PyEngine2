try:
    from PyEngine2.libs import *
    from PyEngine2.main_widget import Window
    from PyEngine2.default_classes import *
    from PyEngine2.widgets import Frame
except ModuleNotFoundError:
    from libs import *
    from main_widget import Window
    from default_classes import *
    from widgets import Frame


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
            
class MiniWindow(Frame):
    def __init__(self, win, 
                mode = "px", 
                coords = [100, 100], 
                visibility = False,
                color = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                font = DEFAULT, 
                width = DEFAULT, 
                height = DEFAULT, 
                labelAnchor = DEFAULT, 
                highlightcolor = DEFAULT, 
                highlightthickness = DEFAULT, 
                text = DEFAULT):
                
        # try:
        #     from PyEngine2.widgets import Frame
        # except ModuleNotFoundError:
        #     from widgets import Frame

        self.__window1__ = win
        self.mode = mode
        self.visibility = visibility
        self.coords = coords
        self.color = color
        self.border = border
        self.bordertype = bordertype
        self.font = font
        self.width = width
        self.height = height
        self.labelAnchor = labelAnchor
        self.highlightcolor = highlightcolor
        self.highlightthickness = highlightthickness
        self.text = text
        self.__objectList__ = []

        if self.visibility:
            self.__object__ = BaseLibrary.LabelFrame(self.__window1__.__window__)
        else:
            self.__object__ = BaseLibrary.Frame(self.__window1__.__window__)
        self.__window__ = self.__object__
        self.__canvas__ = BaseLibrary.Canvas(self.__window__)
        self.__canvas__.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        self.value_change(self.__window__, mode, coords, visibility, color, border, bordertype, font, width, height, labelAnchor, highlightcolor, highlightthickness, text)

    def clear(self):
        self.__canvas__.delete("all")

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

        else:
            raise CantDrawWrongFormatError(obj)

class Toplevel(Window):
    def __init__(self, win, title = "New freaking window", winsize = "200x200+100+100", bg = "#ffffff", resizable = [True, True]):
        self.__objectList__ = []
        self.bg = bg
        self.resizable = resizable
        self.winsize = winsize
        self.title = title
        self.__window1__ = win
        self.__window__ = BaseLibrary.Toplevel(self.__window1__.__window__)
        self.__window__.config(bg = bg)
        self.__window__.title(title)
        self.__window__.geometry(winsize)
        self.__window__.resizable(resizable[0], resizable[1])
        self.__camera__ = __Camera__([0, 0], winsize)
        self.__object__ = self.__window__


        self.__canvas__ = BaseLibrary.Canvas(bg = bg)
