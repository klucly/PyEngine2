try:
    from PyEngine2.libs import *
except ModuleNotFoundError:
    from libs import *
# from PyEngine2.canvas_classes import Rectangle, Oval, Line, OvalSector, OvalSegment, Arc, Polygon, Sprite, Circle

class DEFAULT():
    def __init__(self): pass


class OnClickDefaultWindowClass():
    def on_click(self, func, button = 1):self.__object__.bind(f"<Button-{button}>", func)


class DefaultCanvasObject():

    def __classinfo__(self): return "DefaultCanvasObject"
            
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

        outcoords = self.coords

        for i in range(self.__coords__.__len__()):
            if i in coords:
                outcoords[i] = coords[i]
            
        self.value_change(coords = outcoords)
        
    def value_change(self, mode = DEFAULT, coords = DEFAULT, bg = DEFAULT, border = DEFAULT, outline = DEFAULT, angle = DEFAULT):

        if angle == DEFAULT:
            angle = self.angle
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

        self.__init__(self.__win__, mode, coords, bg, border, outline, angle)

    def on_click(self, win, func, button = 1): win.__canvas__.tag_bind(self.__canvas_obj__, f"<Button-{button}>", lambda event: func())

    def show(self):
        
        if self.__class__ == Rectangle:
            self.__canvas_obj__ =  self.__canvas__.create_polygon(self.__coords__, fill = self.bg, width = self.border, outline = self.outline)

        elif self.__class__ == Oval:
            self.__canvas_obj__ = self.__canvas__.create_oval(self.__coords__, fill = self.bg, width = self.border, outline = self.outline)

        elif self.__class__ == Line:
            self.__canvas_obj__ = self.__canvas__.create_line(self.__coords__, width = self.border, fill = self.color)

        elif self.__class__ == OvalSector:
            self.__canvas_obj__ = self.__canvas__.create_arc(self.__coords__, start = self.start_angle, extent = self.angle, fill = self.bg, width = self.border, outline = self.outline)

        elif self.__class__ == OvalSegment:
            self.__canvas_obj__ = self.__canvas__.create_arc(self.__coords__, style = BaseLibrary.CHORD, start = self.start_angle, extent = self.angle, fill = self.bg, width = self.border, outline = self.outline)

        elif self.__class__ == Arc:
            self.__canvas_obj__ = self.__canvas__.create_arc(self.__coords__, style = BaseLibrary.ARC, start = self.start_angle, extent = self.angle, outline = self.color, width = self.border)

        elif self.__class__ == Polygon:
            self.__canvas_obj__ = self.__canvas__.create_polygon(self.__coords__, fill = self.bg, width = self.border, outline = self.outline)

        elif self.__class__ == Sprite:
            self.__canvas_obj__ = self.__canvas__.create_image(self.__coords__[0], self.__coords__[1], image = self.__image__)

        elif self.__class__ == Circle:
            self.__canvas_obj__ = self.__canvas__.create_oval(self.__coords__, fill = self.bg, width = self.border, outline = self.outline)


class CantDrawWrongFormatError(Exception):
    def __init__(self, obj): pass


class WrongModeError(Exception):
    def __init__(self, obj): pass


class DefaultWindowObject(OnClickDefaultWindowClass):

    def __classinfo__(self): return "DefaultWindowObject"

    def set_position(self, coords):
        outcoords = self.coords

        if coords.__class__ == dict:

            for i in range(self.coords.__len__()):
                if i in coords:
                    outcoords[i] = coords[i]
            self.value_change(coords = outcoords)
            self.__object__.place(x = outcoords[0], y = outcoords[1])
                
        elif coords.__class__ == list:

            self.value_change(coords = coords)
            self.__object__.place(x = coords[0], y = coords[1])

    def move(self, step, vector = "x"):

        if vector == "x":
            self.set_position({0 : self.coords[0]+step})

        if vector == "y":
            self.set_position({1 : self.coords[1]+step})

    # def show(self):
        
    #     if self.__class__ == Menu:
    #         self.__window__.config(menu = self.__object__)

    #     elif self.coords.__len__() == 2:
    #         if self.mode == "px":
    #             self.__object__.place(x = self.coords[0], y = self.coords[1])
    #         elif self.mode == "%":
    #             self.__object__.place(relx = self.coords[0], rely = self.coords[1])

    #     elif self.coords.__len__() == 4:
    #         if self.mode == "px":
    #             self.__object__.place(x = self.coords[0], y = self.coords[1], width = self.coords[2], height = self.coords[3])
    #         elif self.mode == "%":
    #             self.__object__.place(relx = self.coords[0], rely = self.coords[1], relwidth = self.coords[2], relheight = self.coords[3])

    def _showraw(self, **kw): self.__object__.place(**kw)

    def _show_pack(self, **kw): self.__object__.pack(self.__window__, **kw)


class Just(DefaultWindowObject):
    def __init__(self, obj, mode = DEFAULT, coords = DEFAULT):
        self.__window__ = obj
        self.__object__ = obj
        if mode != DEFAULT:
            self.mode = mode
        if coords != DEFAULT:
            self.coords = coords

    def __classinfo__(self):
        return "DefaultWindowObject"
