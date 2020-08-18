try:
    from PyEngine2.libs import *
    from PyEngine2 import default_classes as default
    from PyEngine2.main_widget import Window
    from PyEngine2 import canvas_classes as canvas
    from PyEngine2 import widgets as window
    import PyEngine2.physics
    from PyEngine2 import other_classes as other
except ModuleNotFoundError:
    from libs import *
    import default_classes as default
    from main_widget import Window
    import canvas_classes as canvas
    import widgets as window
    import physics
    import other_classes as other

# from PyEngine2 import other_classes as other

#=================================#
#---------PyEngine2 Alpha---------#
#---------creator: klucly---------#
#=================================#

if __name__ == "__main__":
    import gui