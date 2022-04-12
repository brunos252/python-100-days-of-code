"""
args, kwargs
tkinter - GUI, comes with Python
"""


# arguments can have default values
def my_function(a=1, b=2, c=3):
    pass


# args, can be any number of arguments
# it is a tuple, can be called anything, e.g. *numbers
# since it is a tuple, can be called like args[1]
def add(*args):
    for n in args:
        print(n)


# kwargs, it is a dictionary
# kwargs["name"], for key, value in kwargs.items()
# with dict, instead of dict["value"] we can use key.get("value", "default"),
# if we dont set default, it is None
def calculate(**kwargs):
    pass

# Tkinter has many Layout Managers; Pack, Place, Grid
# Pack - next to each other, starts from top, difficult to specify precise position
# Place - uses coordinates, button.place(x=100, y=100)
# Grid - any number of columns and rows
#       - button.grid(colum=0, row=0)
# - cant use grid and pack at the same time

# add padding:
# window.config(padx = 20, pady = 30)
