import tkinter as BaseLibrary
from tkinter import DISABLED, ACTIVE, NORMAL, LEFT, CENTER, RIGHT, SUNKEN, RAISED, GROOVE, RIDGE, FLAT, X, Y
from tkinter import IntVar, StringVar, BooleanVar
from tkinter import HORIZONTAL, VERTICAL, BROWSE, SINGLE, MULTIPLE, EXTENDED, WORD, CHAR, END, BOTH, BOTTOM, TOP, LEFT, RIGHT
from tkinter import filedialog as __filedialog__
import keyboard
from tkinter import messagebox
import math
import pymunk as basephysicsengine
DYNAMIC = basephysicsengine.Body.DYNAMIC
KINEMATIC = basephysicsengine.Body.KINEMATIC
STATIC = basephysicsengine.Body.STATIC
try:
    from PyEngine2.canvas_classes import Rectangle, Oval, Polygon, OvalSegment, OvalSector, Arc, Line
except ModuleNotFoundError:
    from canvas_classes import Rectangle, Oval, Polygon, OvalSegment, OvalSector, Arc, Line

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
