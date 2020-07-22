import tkinter as BaseLibrary
from tkinter import DISABLED, ACTIVE, NORMAL, LEFT, CENTER, RIGHT, SUNKEN, RAISED, GROOVE, RIDGE, FLAT
from tkinter import IntVar, StringVar, BooleanVar
from tkinter import HORIZONTAL, VERTICAL, BROWSE, SINGLE, MULTIPLE, EXTENDED, WORD, CHAR, END
import keyboard
from tkinter import messagebox
import math

#=================================#
#---------PyEngine Alpha----------#
#---------creator: klucly---------#
#=================================#

class DEFAULT():
    def __init__(self): pass


class OnClickDefaultWindowClass():

    def on_click(self, func, button = 1):

        self.__object__.bind(f"<Button-{button}>", func)


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

    def __classinfo__(self):
        return "DefaultCanvasObject"
            
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
        # if angle == None:
        #     angle = self.__angle__

        self.__init__(self.__win__, mode, coords, bg, border, outline, angle)

    def on_click(self, win, func, button = 1):

        win.__canvas__.tag_bind(self.__canvas_obj__, f"<Button-{button}>", lambda event: func())


class CantDrawWrongFormatError(Exception):
    def __init__(self, obj): pass


class WrongModeError(Exception):
    def __init__(self, obj): pass


class DefaultWindowObject(OnClickDefaultWindowClass):

    def __classinfo__(self):
        return "DefaultWindowObject"

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


def TEST():
    print("works")

#-------------------------------------------------------------------------------------------------------------------------------------------------------

class Button(DefaultWindowObject):

    def __init__(self, win, 
                mode = "px", 
                coords = [100, 100], 
                text = "button", 
                on_click = DEFAULT, 
                width = DEFAULT, 
                height = DEFAULT, 
                font = DEFAULT, 
                border = DEFAULT, 
                color = DEFAULT, 
                highlightcolor = DEFAULT,
                image = DEFAULT,
                bordertype = DEFAULT,
                active = DEFAULT,
                wraplength = DEFAULT,
                activecolor = DEFAULT):

        self.coords = coords
        self.text = text
        self.border = border
        self.on_click = on_click
        self.mode = mode
        self.font = font
        self.__window__ = win
        self.width = width
        self.height = height
        self.highlightcolor = highlightcolor
        self.color = color
        self.activecolor = activecolor
        self.image = image
        self.bordertype = bordertype
        self.active = active
        self.wraplength = wraplength

        self.__object__ = BaseLibrary.Button(self.__window__.__window__, text = text)

        self.value_change(self.coords, self.text, self.on_click, self.width, self.height, self.font, self.border, self.color, self.highlightcolor, self.image, self.bordertype, self.active, self.wraplength, self.activecolor)

    def value_change(self, coords = DEFAULT, 
                text = DEFAULT, 
                on_click = DEFAULT, 
                width = DEFAULT, 
                height = DEFAULT, 
                font = DEFAULT, 
                border = DEFAULT, 
                color = DEFAULT, 
                highlightcolor = DEFAULT,
                image = DEFAULT,
                bordertype = DEFAULT,
                active = DEFAULT,
                wraplength = DEFAULT,
                activecolor = DEFAULT, *kw):
        
        if on_click != DEFAULT:
            self.__object__["command"] = on_click

        if text != DEFAULT:
            self.__object__["text"] = text

        if width != DEFAULT:
            self.__object__["width"] = width
            
        if height != DEFAULT:
            self.__object__["height"] = height

        if border != DEFAULT:
            self.__object__["bd"] = border
            
        if font != DEFAULT:
            self.__object__["font"] = font

        if highlightcolor != DEFAULT:
            self.__object__["highlightcolor"] = highlightcolor

        if image != DEFAULT:
            self.__object__["image"] = image

        if bordertype != DEFAULT:
            self.__object__["relief"] = bordertype

        if active != DEFAULT:
            self.__object__["state"] = active

        if wraplength != DEFAULT:
            self.__object__["wraplength"] = wraplength

        if color != DEFAULT:

            if "bg" in color:
                self.__object__["bg"] = color["bg"]
            if "fg" in color:
                self.__object__["fg"] = color["fg"]
                
        if activecolor != DEFAULT:

            if "bg" in activecolor:
                self.__object__["activebackground"] = activecolor["bg"]
            if "fg" in activecolor:
                self.__object__["activeforeground"] = activecolor["fg"]

    def flash(self):
        self.__object__.flash()



class Label(DefaultWindowObject):

    def __init__(self, win, 
                mode = "px", 
                coords = [100, 100], 
                text = "text", 
                height = DEFAULT, 
                width = DEFAULT, 
                border = DEFAULT, 
                color = DEFAULT, 
                image = DEFAULT, 
                anchor = DEFAULT, 
                font = DEFAULT, 
                wraplength = DEFAULT):

        self.coords = coords
        self.text = text
        self.mode = mode
        self.height = height
        self.width = width
        self.border = border
        self.color = color
        self.image = image
        self.anchor = anchor
        self.font = font
        self.__window__ = win
        self.wraplength = wraplength

        self.__object__ = BaseLibrary.Label(self.__window__.__window__, text = self.text)

        self.value_change(self.coords, self.text, self.height, self.width, self.border, self.color, self.image, self.anchor, self.font, self.wraplength)

    def value_change(self, coords = DEFAULT,
                text = DEFAULT, 
                height = DEFAULT, 
                width = DEFAULT, 
                border = DEFAULT, 
                color = DEFAULT, 
                image = DEFAULT, 
                anchor = DEFAULT, 
                font = DEFAULT, 
                wraplength = DEFAULT):
        
        
        if coords != DEFAULT:
            self.coords = coords
        if height != DEFAULT:
            self.__object__["height"] = height
        
        if width != DEFAULT:
            self.__object__["width"] = width
        
        if border != DEFAULT:
            self.__object__["bd"] = border
        
        if image != DEFAULT:
            self.__object__["image"] = image
        
        if anchor != DEFAULT:
            self.__object__["anchor"] = anchor
        
        if font != DEFAULT:
            self.__object__["font"] = font
        
        if wraplength != DEFAULT:
            self.__object__["wraplength"] = wraplength

        if color != DEFAULT:

            if "bg" in color:
                self.__object__["bg"] = color["bg"]
            if "fg" in color:
                self.__object__["fg"] = color["fg"]



class Entry(DefaultWindowObject):

    def __init__(self, win, 
                mode = "px", 
                coords = [100, 100], 
                color = DEFAULT, 
                border = DEFAULT, 
                font = DEFAULT, 
                bordertype = DEFAULT, 
                selectcolor = DEFAULT, 
                show = DEFAULT,
                active = DEFAULT,
                width = DEFAULT):

        self.__window__ = win
        self.coords = coords
        self.color = color
        self.mode = mode
        self.border = border
        self.font = font
        self.bordertype = bordertype
        self.selectcolor = selectcolor
        self.show = show
        self.active = active
        self.width = width

        self.__object__ = BaseLibrary.Entry(self.__window__.__window__)

        self.value_change(self.__window__, self.coords, self.color, self.border, self.font, self.bordertype, self.selectcolor, self.show, self.active, self.width)

    def value_change(self, win = DEFAULT, 
                coords = DEFAULT, 
                color = DEFAULT, 
                border = DEFAULT, 
                font = DEFAULT, 
                bordertype = DEFAULT, 
                selectcolor = DEFAULT, 
                show = DEFAULT,
                active = DEFAULT,
                width = DEFAULT):

        if coords != DEFAULT:
            self.coords = coords
        
        if border != DEFAULT:
            self.__object__["bd"] = border
        
        if font != DEFAULT:
            self.__object__["font"] = font
        
        if bordertype != DEFAULT:
            self.__object__["relief"] = bordertype
        
        if show != DEFAULT:
            self.__object__["show"] = show
        
        if active != DEFAULT:
            self.__object__["state"] = active
        
        if width != DEFAULT:
            self.__object__["width"] = width

        if color != DEFAULT:

            if BG in color:
                self.__object__["bg"] = color[BG]
            if FG in color:
                self.__object__["fg"] = color[FG]
                
        if selectcolor != DEFAULT:

            if BG in selectcolor:
                self.__object__["selectbackground"] = selectcolor[BG]
            if FG in selectcolor:
                self.__object__["selectforeground"] = selectcolor[FG]

    def get(self):
        return self.__object__.get()



class RadioButton(DefaultWindowObject):

    def __init__(self, win, 
                mode = "px", 
                coords = [100, 100], 
                color = DEFAULT, 
                activecolor = DEFAULT, 
                highlightcolor = DEFAULT, 
                selectcolor = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                on_change_value = DEFAULT, 
                font = DEFAULT, 
                width = DEFAULT, 
                height = DEFAULT, 
                image = DEFAULT, 
                active = DEFAULT, 
                text = DEFAULT, 
                variable = DEFAULT, 
                value = DEFAULT, 
                wraplength = DEFAULT, 
                button = DEFAULT):
        
        self.coords = coords
        self.button = button
        self.color = color
        self.activecolor = activecolor
        self.highlightcolor = highlightcolor
        self.selectcolor = selectcolor
        self.border = border
        self.bordertype = bordertype
        self.on_change_value = on_change_value
        self.font = font
        self.width = width
        self.height = height
        self.image = image
        self.active = active
        self.text = text
        self.variable = variable
        self.value = value
        self.wraplength = wraplength
        self.__window__ = win
        self.mode = mode
        
        self.__object__ = BaseLibrary.Radiobutton(self.__window__.__window__)

        self.value_change(self.__window__, self.mode, self.coords, self.color, self.activecolor, self.highlightcolor, self.selectcolor, self.border, self.bordertype, self.on_change_value, self.font, self.width, self.height, self.image, self.active, self.text, self.variable, self.value, self.wraplength, self.button)

    def value_change(self, win = DEFAULT, 
                mode = DEFAULT, 
                coords = DEFAULT, 
                color = DEFAULT, 
                activecolor = DEFAULT, 
                highlightcolor = DEFAULT, 
                selectcolor = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                on_change_value = DEFAULT, 
                font = DEFAULT, 
                width = DEFAULT, 
                height = DEFAULT, 
                image = DEFAULT, 
                active = DEFAULT, 
                text = DEFAULT, 
                variable = DEFAULT, 
                value = DEFAULT, 
                wraplength = DEFAULT, 
                button = DEFAULT):

        if coords != DEFAULT:
            self.coords = coords
        
        if button != DEFAULT:
            self.__object__["indicatoron"] = not(button)

        if mode != DEFAULT:
            self.mode = mode

        if border != DEFAULT:
            self.__object__["borderwidth"] = border

        if bordertype != DEFAULT:
            self.__object__["relief"] = bordertype

        if on_change_value != DEFAULT:
            self.__object__["relief"] = on_change_value

        if font != DEFAULT:
            self.__object__["font"] = font

        if width != DEFAULT:
            self.__object__["width"] = width

        if height != DEFAULT:
            self.__object__["height"] = height

        if image != DEFAULT:
            self.__object__["image"] = image

        if active != DEFAULT:
            self.__object__["relief"] = active

        if text != DEFAULT:
            self.__object__["text"] = text

        if variable != DEFAULT:
            self.__object__["variable"] = variable

        if value != DEFAULT:
            self.__object__["value"] = value

        if wraplength != DEFAULT:
            self.__object__["wraplength"] = wraplength

        if color != DEFAULT:

            if BG in color:
                self.__object__["bg"] = color[BG]
            if FG in color:
                self.__object__["fg"] = color[FG]

        if activecolor != DEFAULT:

            if BG in activecolor:
                self.__object__["activebackground"] = activecolor[BG]
            if FG in activecolor:
                self.__object__["activeforeground"] = activecolor[FG]

        if highlightcolor != DEFAULT:

            if BG in highlightcolor:
                self.__object__["highlightbackground"] = highlightcolor[BG]
            if FG in highlightcolor:
                self.__object__["highlightcolor"] = highlightcolor[FG]

        if selectcolor != DEFAULT:
            self.__object__["selectcolor"] = selectcolor

    def deselect(self):
        self.__object__.deselect()

    def select(self):
        self.__object__.select()

    def flash(self):
        self.__object__.flash()

    def invoke(self):
        self.__object__.invoke()



class CheckButton(DefaultWindowObject):

    def __init__(self, win, 
                mode = "px", 
                coords = [100, 100], 
                color = DEFAULT, 
                activecolor = DEFAULT, 
                highlightcolor = DEFAULT, 
                selectcolor = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                image = DEFAULT, 
                onvalue = DEFAULT, 
                offvalue = DEFAULT, 
                active = DEFAULT, 
                text = DEFAULT, 
                variable = DEFAULT, 
                width = DEFAULT, 
                height = DEFAULT, 
                wraplength = DEFAULT, 
                font = DEFAULT, 
                button = DEFAULT):


        self.coords = coords
        self.offvalue = offvalue
        self.onvalue = onvalue
        self.color = color
        self.activecolor = activecolor
        self.highlightcolor = highlightcolor
        self.selectcolor = selectcolor
        self.border = border
        self.bordertype = bordertype
        self.font = font
        self.width = width
        self.height = height
        self.image = image
        self.active = active
        self.text = text
        self.variable = variable
        self.wraplength = wraplength
        self.__window__ = win
        self.button = button
        self.mode = mode

        self.__object__ = BaseLibrary.Checkbutton(self.__window__.__window__)

        self.value_change(self.__window__, self.mode, self.coords, self.color, self.activecolor, self.highlightcolor, self.selectcolor, self.border, self.bordertype, self.image, self.onvalue, self.offvalue, self.active, self.text, self.variable, self.width, self.height, self.wraplength, self.font, self.button)

    def value_change(self, win, 
                mode = DEFAULT, 
                coords = DEFAULT, 
                color = DEFAULT, 
                activecolor = DEFAULT, 
                highlightcolor = DEFAULT, 
                selectcolor = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                image = DEFAULT, 
                onvalue = DEFAULT, 
                offvalue = DEFAULT, 
                active = DEFAULT, 
                text = DEFAULT, 
                variable = DEFAULT, 
                width = DEFAULT, 
                height = DEFAULT, 
                wraplength = DEFAULT, 
                font = DEFAULT, 
                button = DEFAULT):

        if coords != DEFAULT:
            self.coords = coords

        if mode != DEFAULT:
            self.mode = mode

        if button != DEFAULT:
            self.__object__["indicatoron"] = not(button)

        if border != DEFAULT:
            self.__object__["borderwidth"] = border

        if bordertype != DEFAULT:
            self.__object__["relief"] = bordertype

        if font != DEFAULT:
            self.__object__["font"] = font

        if width != DEFAULT:
            self.__object__["width"] = width

        if height != DEFAULT:
            self.__object__["height"] = height

        if image != DEFAULT:
            self.__object__["image"] = image

        if active != DEFAULT:
            self.__object__["state"] = active

        if text != DEFAULT:
            self.__object__["text"] = text

        if variable != DEFAULT:
            self.__object__["variable"] = variable

        if wraplength != DEFAULT:
            self.__object__["wraplength"] = wraplength

        if color != DEFAULT:

            if BG in color:
                self.__object__["bg"] = color[BG]
            if FG in color:
                self.__object__["fg"] = color[FG]

        if activecolor != DEFAULT:

            if BG in activecolor:
                self.__object__["activebackground"] = activecolor[BG]
            if FG in activecolor:
                self.__object__["activeforeground"] = activecolor[FG]

        if highlightcolor != DEFAULT:

            if BG in highlightcolor:
                self.__object__["highlightbackground"] = highlightcolor[BG]
            if FG in highlightcolor:
                self.__object__["highlightcolor"] = highlightcolor[FG]

        if selectcolor != DEFAULT:
            self.__object__["selectcolor"] = selectcolor

    def deselect(self):
        self.__object__.deselect()

    def select(self):
        self.__object__.select()

    def flash(self):
        self.__object__.flash()

    def invoke(self):
        self.__object__.invoke()

    def toggle(self):
        self.__object__.toggle()



class Scale(DefaultWindowObject):

    def __init__(self, win, 
                mode = "px",
                coords = [100, 100], 
                notnumber = False, 
                color = DEFAULT, 
                on_move = DEFAULT, 
                activecolor = DEFAULT, 
                digits = DEFAULT, 
                font = DEFAULT, 
                border = DEFAULT, 
                highlightcolor = DEFAULT, 
                length = DEFAULT, 
                orient = DEFAULT, 
                bordertype = DEFAULT, 
                repeatdelay = DEFAULT, 
                resolution = DEFAULT, 
                showvalue = DEFAULT, 
                sliderlength = DEFAULT, 
                active = DEFAULT, 
                takefocus = DEFAULT, 
                tickinterval = DEFAULT, 
                to = DEFAULT, 
                troughcolor = DEFAULT, 
                variable = DEFAULT, 
                width = DEFAULT):

        self.__window__ = win
        self.coords = coords
        self.notnumber = notnumber
        self.color = color
        self.on_move = on_move
        self.activecolor = activecolor
        self.digits = digits
        self.font = font
        self.mode = mode
        self.border = border
        self.highlightcolor = highlightcolor
        self.length = length
        self.orient = orient
        self.bordertype = bordertype
        self.repeatdelay = repeatdelay
        self.resolution = resolution
        self.showvalue = showvalue
        self.sliderlength = sliderlength
        self.active = active
        self.takefocus = takefocus
        self.tickinterval = tickinterval
        self.to = to
        self.troughcolor = troughcolor
        self.variable = variable
        self.width = width

        if notnumber:
            self.__object__ = BaseLibrary.Scrollbar(self.__window__.__window__)
        else:
            self.__object__ = BaseLibrary.Scale(self.__window__.__window__)

        self.value_change(self.__window__.__window__, self.mode, self.coords, self.notnumber, self.color, self.on_move, self.activecolor, self.digits, self.font, self.border, self.highlightcolor, self.length, self.orient, self.bordertype, self.repeatdelay, self.resolution, self.showvalue, self.sliderlength, self.active, self.takefocus, self.tickinterval, self.to, self.troughcolor, self.variable, self.width)

    def value_change(self, win = DEFAULT, 
                mode = DEFAULT,
                coords = DEFAULT, 
                notnumber = DEFAULT,
                color = DEFAULT, 
                on_move = DEFAULT, 
                activecolor = DEFAULT, 
                digits = DEFAULT, 
                font = DEFAULT, 
                border = DEFAULT, 
                highlightcolor = DEFAULT, 
                length = DEFAULT, 
                orient = DEFAULT, 
                bordertype = DEFAULT, 
                repeatdelay = DEFAULT, 
                resolution = DEFAULT, 
                showvalue = DEFAULT, 
                sliderlength = DEFAULT, 
                active = DEFAULT, 
                takefocus = DEFAULT, 
                tickinterval = DEFAULT, 
                to = DEFAULT, 
                troughcolor = DEFAULT, 
                variable = DEFAULT, 
                width = DEFAULT):

        if coords != DEFAULT:
            self.coords = coords

        if notnumber != DEFAULT:
            self.notnumber = notnumber

        if mode != DEFAULT:
            self.mode = mode

        if on_move != DEFAULT:
            self.__object__["command"] = on_move

        if digits != DEFAULT and not notnumber:
            self.__object__["digits"] = digits

        if font != DEFAULT and not notnumber:
            self.__object__["font"] = font

        if border != DEFAULT:
            self.__object__["bd"] = border

        if length != DEFAULT and not notnumber:
            self.__object__["length"] = length

        if orient != DEFAULT:
            self.__object__["orient"] = orient

        if bordertype != DEFAULT:
            self.__object__["relief"] = bordertype

        if repeatdelay != DEFAULT:
            self.__object__["repeatdelay"] = repeatdelay

        if resolution != DEFAULT and not notnumber:
            self.__object__["resolution"] = resolution

        if showvalue != DEFAULT and not notnumber:
            self.__object__["showvalue"] = showvalue

        if sliderlength != DEFAULT and not notnumber:
            self.__object__["sliderlength"] = sliderlength

        if active != DEFAULT:
            self.__object__["state"] = active

        if takefocus != DEFAULT:
            self.__object__["takefocus"] = takefocus

        if tickinterval != DEFAULT and not notnumber:
            self.__object__["tickinterval"] = tickinterval

        if to != DEFAULT and not notnumber:
            self.__object__["to"] = to

        if troughcolor != DEFAULT:
            self.__object__["troughcolor"] = troughcolor

        if variable != DEFAULT:
            self.__object__["variable"] = variable

        if width != DEFAULT:
            self.__object__["width"] = width

        if color != DEFAULT:

            if BG in color:
                self.__object__["bg"] = color[BG]
            if FG in color:
                self.__object__["fg"] = color[FG]

        if activecolor != DEFAULT:

            if BG in color:
                self.__object__["activebackground"] = activecolor[BG]
            if FG in color:
                self.__object__["activeforeground"] = activecolor[FG]

        if highlightcolor != DEFAULT:

            if BG in color:
                self.__object__["highlightbackground"] = highlightcolor[BG]
            if FG in color:
                self.__object__["highlightcolor"] = highlightcolor[FG]
        
    def set(self, value):
        self.__object__.set(value)

    def get(self):
        return self.__object__.get()
        


class Text(DefaultWindowObject):

    def __init__(self, win = DEFAULT, 
                mode = "px", 
                coords = [100, 100], 
                color = DEFAULT, 
                exportselection = DEFAULT, 
                font = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                height = DEFAULT, 
                highlightcolor = DEFAULT, 
                highlightthickness = DEFAULT, 
                insertbackground = DEFAULT, 
                insertborderwidth = DEFAULT, 
                insertontime = DEFAULT, 
                insertwidth = DEFAULT, 
                selectcolor = DEFAULT, 
                active = DEFAULT, 
                tabs = DEFAULT, 
                width = DEFAULT, 
                wrap = DEFAULT, 
                xscrollcommand = DEFAULT, 
                yscrollcommand = DEFAULT):

        self.__window__ = win
        self.mode = mode
        self.coords = coords
        self.color = color
        self.exportselection = exportselection
        self.font = font
        self.border = border
        self.bordertype = bordertype
        self.height = height
        self.highlightcolor = highlightcolor
        self.highlightthickness = highlightthickness
        self.insertbackground = insertbackground
        self.insertborderwidth = insertborderwidth
        self.insertontime = insertontime
        self.insertwidth = insertwidth
        self.selectcolor = selectcolor
        self.active = active
        self.tabs = tabs
        self.width = width
        self.wrap = wrap
        self.xscrollcommand = xscrollcommand
        self.yscrollcommand = yscrollcommand

        self.__object__ = BaseLibrary.Text(self.__window__.__window__)
        self.tag_config = self.__object__.tag_config

        self.value_change(self.__window__, mode, coords, color, exportselection, font, border, bordertype, height, highlightcolor, highlightthickness, insertbackground, insertborderwidth, insertontime, insertwidth, selectcolor, active, tabs, width, wrap, xscrollcommand, yscrollcommand)

    def value_change(self, win = DEFAULT, 
                mode = DEFAULT, 
                coords = DEFAULT, 
                color = DEFAULT, 
                exportselection = DEFAULT, 
                font = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                height = DEFAULT, 
                highlightcolor = DEFAULT, 
                highlightthickness = DEFAULT, 
                insertbackground = DEFAULT, 
                insertborderwidth = DEFAULT, 
                insertontime = DEFAULT, 
                insertwidth = DEFAULT, 
                selectcolor = DEFAULT, 
                active = DEFAULT, 
                tabs = DEFAULT, 
                width = DEFAULT, 
                wrap = DEFAULT, 
                xscrollcommand = DEFAULT, 
                yscrollcommand = DEFAULT):

        if coords != DEFAULT:
            self.coords = coords

        if mode != DEFAULT:
            self.mode = mode

        if exportselection != DEFAULT:
            self.__object__["exportselection"] = exportselection

        if font != DEFAULT:
            self.__object__["font"] = font

        if border != DEFAULT:
            self.__object__["bd"] = border

        if bordertype != DEFAULT:
            self.__object__["relief"] = bordertype

        if height != DEFAULT:
            self.__object__["height"] = height

        if highlightthickness != DEFAULT:
            self.__object__["highlightthickness"] = highlightthickness

        if insertborderwidth != DEFAULT:
            self.__object__["insertborderwidth"] = insertborderwidth

        if insertontime != DEFAULT:
            self.__object__["insertontime"] = insertontime

        if insertwidth != DEFAULT:
            self.__object__["insertwidth"] = insertwidth

        if active != DEFAULT:
            self.__object__["state"] = active

        if tabs != DEFAULT:
            self.__object__["tabs"] = tabs

        if width != DEFAULT:
            self.__object__["width"] = width

        if wrap != DEFAULT:
            self.__object__["wrap"] = wrap

        if xscrollcommand != DEFAULT:
            self.__object__["xscrollcommand"] = xscrollcommand

        if yscrollcommand != DEFAULT:
            self.__object__["yscrollcommand"] = yscrollcommand

        if color != DEFAULT:

            if BG in color:
                self.__object__["bg"] = color[BG]

            if FG in color:
                self.__object__["fg"] = color[FG]

        if highlightcolor != DEFAULT:

            if BG in color:
                self.__object__["highlightbackground"] = highlightcolor[BG]

            if FG in color:
                self.__object__["highlightcolor"] = highlightcolor[FG]

        if insertbackground != DEFAULT:
            self.__object__["insertbackground"] = insertbackground

        if selectcolor != DEFAULT:

            if BG in selectcolor:
                self.__object__["selectbackground"] = selectcolor[BG]

            if FG in selectcolor:
                self.__object__["selectcolor"] = selectcolor[FG]
        
    def delete(self, startindex, endindex):
        self.__object__.delete(startindex, endindex)

    def get(self, startindex, endindex):
        return self.__object__.get(startindex, endindex)

    def index(self, index):
        return self.__object__.index(index)

    def insert(self, index, chars):
        self.__object__.insert(index, chars)

    def see(self, index):
        return self.__object__.see(index)

    def mark_gravity(self, mark):
        return self.__object__.mark_gravity(mark)

    def mark_names(self):
        return self.__object__.mark_names()

    def mark_set(self, mark, index):
        return self.__object__.mark_set(mark, index)

    def mark_unset(self, marks):
        return self.__object__.mark_unset(marks)

    def tag_add(self, tagname, startindex, endindex):
        return self.__object__.tag_add(tagname, startindex, endindex)

    def tag_delete(self, tag):
        return self.__object__.tag_delete(tag)

    def tag_remove(self, tag, startindex, endindex):
        return self.__object__.tag_remove(tag, startindex, endindex)



class Frame(DefaultWindowObject):

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

        if self.visibility:
            self.__object__ = BaseLibrary.LabelFrame(self.__window1__.__window__)
        else:
            self.__object__ = BaseLibrary.Frame(self.__window1__.__window__)
        self.__window__ = self.__object__

        self.value_change(self.__window__, mode, coords, visibility, color, border, bordertype, font, width, height, labelAnchor, highlightcolor, highlightthickness, text)

    def value_change(self, win = DEFAULT, 
                mode = DEFAULT, 
                coords = DEFAULT, 
                visibility = DEFAULT,
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
        
        if mode != DEFAULT:
            self.mode = mode

        if coords != DEFAULT:
            self.coords = coords

        if visibility != DEFAULT:
            self.visibility = visibility

        if border != DEFAULT:
            self.__object__["bd"] = border

        if bordertype != DEFAULT:
            self.__object__["relief"] = bordertype

        if font != DEFAULT and self.visibility:
            self.__object__["font"] = font

        if width != DEFAULT:
            self.__object__["width"] = width

        if height != DEFAULT:
            self.__object__["height"] = height

        if labelAnchor != DEFAULT and self.visibility:
            self.__object__["labelAnchor"] = labelAnchor

        if highlightthickness != DEFAULT:
            self.__object__["highlightthickness"] = highlightthickness

        if text != DEFAULT and self.visibility:
            self.__object__["text"] = text

        if color != DEFAULT:

            if BG in color:
                self.__object__["bg"] = color[BG]

            if FG in color:
                self.__object__["fg"] = color[FG]

        if highlightcolor != DEFAULT:

            if BG in highlightcolor:
                self.__object__["highlightbackground"] = highlightcolor[BG]

            if FG in highlightcolor:
                self.__object__["highlightcolor"] = highlightcolor[FG]



class ListBox(DefaultWindowObject):

    def __init__(self, win, 
                mode = "px", 
                coords = [100, 100], 
                color = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                font = DEFAULT, 
                width = DEFAULT, 
                height = DEFAULT, 
                highlightcolor = DEFAULT, 
                highlightthickness = DEFAULT, 
                selectcolor = DEFAULT, 
                selectmode = DEFAULT, 
                xscrollcommand = DEFAULT, 
                yscrollcommand = DEFAULT):

        self.__window__ = win
        self.mode = mode
        self.coords = coords
        self.color = color
        self.border = border
        self.bordertype = bordertype
        self.font = font
        self.width = width
        self.height = height
        self.highlightcolor = highlightcolor
        self.highlightthickness = highlightthickness
        self.selectcolor = selectcolor
        self.selectmode = selectmode
        self.xscrollcommand = xscrollcommand
        self.yscrollcommand = yscrollcommand

        self.__object__ = BaseLibrary.Listbox(self.__window__.__window__)

        self.value_change(self.__window__, mode, coords, color, border, bordertype, font, width, height, highlightcolor, highlightthickness, selectcolor, selectmode, xscrollcommand, yscrollcommand)

        self.activate = self.__object__.activate
        self.curselection = self.__object__.curselection
        self.delete = self.__object__.delete
        self.get = self.__object__.get
        self.index = self.__object__.index
        self.insert = self.__object__.insert
        self.nearest = self.__object__.nearest
        self.see = self.__object__.see
        self.size = self.__object__.size
        self.xview = self.__object__.xview
        self.xview_moveto = self.__object__.xview_moveto
        self.xview_scroll = self.__object__.xview_scroll
        self.yview = self.__object__.yview
        self.yview_moveto = self.__object__.yview_moveto
        self.yview_scroll = self.__object__.yview_scroll

    def value_change(self, win = DEFAULT, 
                mode = DEFAULT, 
                coords = DEFAULT, 
                color = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                font = DEFAULT, 
                width = DEFAULT, 
                height = DEFAULT, 
                highlightcolor = DEFAULT, 
                highlightthickness = DEFAULT, 
                selectcolor = DEFAULT, 
                selectmode = DEFAULT, 
                xscrollcommand = DEFAULT, 
                yscrollcommand = DEFAULT):

        if mode != DEFAULT:
            self.mode = mode
        
        if coords != DEFAULT:
            self.coords = coords

        if border != DEFAULT:
            self.__object__["bd"] = border

        if bordertype != DEFAULT:
            self.__object__["relief"] = bordertype

        if font != DEFAULT:
            self.__object__["font"] = font

        if width != DEFAULT:
            self.__object__["width"] = width

        if height != DEFAULT:
            self.__object__["height"] = height

        if highlightthickness != DEFAULT:
            self.__object__["highlightthickness"] = highlightthickness

        if selectmode != DEFAULT:
            self.__object__["selectmode"] = selectmode

        if xscrollcommand != DEFAULT:
            self.__object__["xscrollcommand"] = xscrollcommand

        if yscrollcommand != DEFAULT:
            self.__object__["yscrollcommand"] = yscrollcommand

        if color != DEFAULT:

            if BG in color:
                self.__object__["bg"] = color[BG]

            if FG in color:
                self.__object__["fg"] = color[FG]

        if highlightcolor != DEFAULT:

            if BG in highlightcolor:
                self.__object__["highlightbackground"] = highlightcolor[BG]

            if FG in highlightcolor:
                self.__object__["highlightcolor"] = highlightcolor[FG]

        if selectcolor != DEFAULT:

            if BG in selectcolor:
                self.__object__["selectbackground"] = selectcolor[BG]

            if FG in selectcolor:
                self.__object__["selectcolor"] = selectcolor[FG]



class Menubutton(DefaultWindowObject):

    def __init__(self, win, 
                mode = "px", 
                coords = [100, 100], 
                color = DEFAULT, 
                activecolor = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                direction = DEFAULT, 
                disabledforeground = DEFAULT, 
                height = DEFAULT, 
                width = DEFAULT, 
                highlightcolor = DEFAULT, 
                menu = DEFAULT, 
                active = DEFAULT, 
                text = DEFAULT, 
                textvariable = DEFAULT, 
                wraplength = DEFAULT):

        self.__window1__ = win
        self.mode = mode
        self.coords = coords
        self.color = color
        self.activecolor = activecolor
        self.border = border
        self.bordertype = bordertype
        self.direction = direction
        self.disabledforeground = disabledforeground
        self.height = height
        self.width = width
        self.highlightcolor = highlightcolor
        self.menu = menu
        self.active = active
        self.text = text
        self.textvariable = textvariable
        self.wraplength = wraplength

        self.__object__ = BaseLibrary.Menubutton(self.__window1__.__window__)
        self.__window__ = self.__object__

        self.value_change(self.__window__, mode, coords, color, activecolor, border, bordertype, direction, disabledforeground, height, width, highlightcolor, menu, active, text, textvariable, wraplength)

    def value_change(self, win = DEFAULT, 
                mode = DEFAULT, 
                coords = DEFAULT, 
                color = DEFAULT, 
                activecolor = DEFAULT, 
                border = DEFAULT, 
                bordertype = DEFAULT, 
                direction = DEFAULT, 
                disabledforeground = DEFAULT, 
                height = DEFAULT, 
                width = DEFAULT, 
                highlightcolor = DEFAULT, 
                menu = DEFAULT, 
                active = DEFAULT, 
                text = DEFAULT, 
                textvariable = DEFAULT, 
                wraplength = DEFAULT):

        if mode != DEFAULT:
            self.mode = mode

        if coords != DEFAULT:
            self.coords = coords

        if border != DEFAULT:
            self.__object__["bd"] = border

        if bordertype != DEFAULT:
            self.__object__["relief"] = bordertype

        if direction != DEFAULT:
            self.__object__["direction"] = direction

        if disabledforeground != DEFAULT:
            self.__object__["disabledforeground"] = disabledforeground

        if height != DEFAULT:
            self.__object__["height"] = height

        if width != DEFAULT:
            self.__object__["width"] = width

        if menu != DEFAULT:
            self.__object__["menu"] = menu.__object__

        if active != DEFAULT:
            self.__object__["state"] = active

        if text != DEFAULT:
            self.__object__["text"] = text

        if textvariable != DEFAULT:
            self.__object__["textvariable"] = textvariable

        if wraplength != DEFAULT:
            self.__object__["wraplength"] = wraplength

        if color != DEFAULT:
            
            if BG in color:
                self.__object__["bg"] = color[BG]
            
            if FG in color:
                self.__object__["fg"] = color[FG]

        if activecolor != DEFAULT:
            
            if BG in activecolor:
                self.__object__["activebackground"] = activecolor[BG]
            
            if FG in activecolor:
                self.__object__["activecolor"] = activecolor[FG]

        if highlightcolor != DEFAULT:
            
            if BG in highlightcolor:
                self.__object__["highlightbackground"] = highlightcolor[BG]
            
            if FG in highlightcolor:
                self.__object__["highlightcolor"] = highlightcolor[FG]



class Menu():

    def __init__(self, win, instructions):

        def readobj(obj, inp, out, recursion):

            def selaretoring(out, obj, recursion, inp):

                command = DEFAULT().__init__
                bg = WHITE
                fg = BLACK
                selectcolor = BLACK
                activebackground = "#0078D7"
                activeforeground = WHITE

                if OPTIONS in inp[obj]:

                    if COMMAND in inp[obj][OPTIONS]:
                        command = inp[obj][OPTIONS][COMMAND]

                    if COLOR in inp[obj][OPTIONS]:

                        if BG in inp[obj][OPTIONS][COLOR]:
                            bg = inp[obj][OPTIONS][COLOR][BG]

                        if FG in inp[obj][OPTIONS][COLOR]:
                            fg = inp[obj][OPTIONS][COLOR][FG]

                    if SELECTCOLOR in inp[obj][OPTIONS]:
                        selectcolor = inp[obj][OPTIONS][SELECTCOLOR]

                    if ACTIVECOLOR in inp[obj][OPTIONS]:

                        if BG in inp[obj][OPTIONS][ACTIVECOLOR]:
                            activebackground = inp[obj][OPTIONS][ACTIVECOLOR][BG]

                        if FG in inp[obj][OPTIONS][ACTIVECOLOR]:
                            activeforeground = inp[obj][OPTIONS][ACTIVECOLOR][FG]

                return command, bg, fg, selectcolor, activebackground, activeforeground
            
            if obj == SEPARATOR:
                
                bg = WHITE
                if BG in inp[obj]:
                    bg = inp[obj][BG]
                
                out[recursion].add_separator(background = bg)
            
            elif inp[obj][MODE] == COMMAND:

                l = selaretoring(out, obj, recursion, inp)
                
                out[recursion].add_command(label = obj, 
                                                command = inp[obj][VALUE][COMMAND], 
                                                background = l[1], 
                                                foreground = l[2], 
                                                activebackground = l[4],
                                                activeforeground = l[5])

            elif inp[obj][MODE] == CHECKBUTTON:

                l = selaretoring(out, obj, recursion, inp)

                out[recursion].add_checkbutton(label = obj, 
                                                variable = inp[obj][VALUE][VARIABLE], 
                                                command = l[0], 
                                                background = l[1], 
                                                foreground = l[2], 
                                                selectcolor = l[3],
                                                activebackground = l[4],
                                                activeforeground = l[5])

            elif inp[obj][MODE] == RADIOBUTTON:

                l = selaretoring(out, obj, recursion, inp)

                out[recursion].add_radiobutton(label = obj, 
                                                variable = inp[obj][VALUE][VARIABLE], 
                                                value = inp[obj][VALUE][VALUE], 
                                                command = l[0], 
                                                background = l[1], 
                                                foreground = l[2], 
                                                selectcolor = l[3],
                                                activebackground = l[4],
                                                activeforeground = l[5])

            elif inp[obj][MODE] == CASCADE:
                
                obj1 = BaseLibrary.Menu(out[recursion], tearoff=0)

                l = selaretoring(out, obj, recursion, inp)

                out[recursion].add_cascade(label = obj, menu = obj1, command = l[0], 
                                                background = l[1], 
                                                foreground = l[2], 
                                                activebackground = l[4],
                                                activeforeground = l[5])

                out.append(obj1)
                recursion += 1
                for inp1 in inp[obj][VALUE]:
                    readobj(inp1, inp[obj][VALUE], out, recursion)

        out = [BaseLibrary.Menu(win.__window__, tearoff=0)]
        for obj in instructions:
            readobj(obj, instructions, out, 0)
                
        self.__window__ = win
        self.__object__ = out[0]

        self.delete = self.__object__.delete
        self.change = self.__object__.entryconfig
        self.index = self.__object__.index
        self.insert_separator = self.__object__.insert_separator
        self.invoke = self.__object__.invoke
        self.type = self.__object__.type
        
    def show(self, x, y):
        self.__object__.post(x, y)

    def __classinfo__(self):
        return "DefaultWindowObject"



class Message():
    
    def info(title, text):
        return messagebox.showinfo(title, text)
    
    def warning(title, text):
        return messagebox.showwarning(title, text)
    
    def error(title, text):
        return messagebox.showerror(title, text)
    
    def question(title, text):
        return messagebox.askquestion(title, text)
    
    def ok_cancel(title, text):
        return messagebox.askokcancel(title, text)
    
    def retry_cancel(title, text):
        return messagebox.askretrycancel (title, text)
    
    def yes_no(title, text):
        return messagebox.askyesno(title, text)
    




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
        self.__coords__ = [0, 0, 0, 0]
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
        self.__camera__ = __Camera__([0, 0], winsize)
        self.__object__ = self.__window__


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

BG = "bg"
FG = "fg"

BLUE = "blue"
RED = "red"
GREEN = "green"
PURPLE = "purple"
BLACK = "black"
WHITE = "white"
GRAY = "gray"
CYAN = "cyan"
VIOLET = "violet"
YELLOW = "yellow"
ORANGE = "orange"
BROWN = "brown"
SILVER = "silver"

MODE = "mode"
CASCADE = "cascade"
CHECKBUTTON = "checkbutton"
COMMAND = "command"
RADIOBUTTON = "radiobutton"
SEPARATOR = "separator"
TEAROFF = "tearoff"
VALUE = "value"
VARIABLE = "variable"
OPTIONS = "options"
COLOR = "color"
ACTIVECOLOR = "activecolor"
BORDER = "border"
BORDERTYPE = "BORDERTYPE"
SELECTCOLOR = "selectcolor"
FONT = "font"