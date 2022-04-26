import os, random, string
from pathlib import Path
import inichecker
inichecker.inichecker()
from tkinter import *
from tkinter.ttk import *
import showresult, noun, verb, adje, play, register, find_index, view
import sys
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        # Just use file=resource_path('rock.png') instead of file='rock.png'
    return os.path.join(base_path, relative_path)



os.chdir(f'{Path.home()}/MadLips/')
# Create object
root = Tk()
root.geometry("1140x570")# Adjust size
bg = PhotoImage(file=resource_path("stardew.png"))# Add image file
canvas1 = Canvas(root, width=400, height=400, bd=0, highlightthickness=0, relief='ridge')# Create Canvas
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")# Display image

# images
btnplay_img = PhotoImage(file=resource_path(r"btnplay.png"))
btnnew_img = PhotoImage(file=resource_path(r"btnnew.png"))
btnview_img = PhotoImage(file=resource_path(r"btnview.png"))
btnexit_img = PhotoImage(file=resource_path(r"btnexit.png"))

# Create Buttons
btnplay = Button(root, image=btnplay_img, command=play.play)
btnnew = Button(root, image=btnnew_img, command=register.register)
btnview = Button(root, image=btnview_img, command=view.view)
btnexit = Button(root, image=btnexit_img, command=root.quit)

# Display Buttons
btnplay_canvas = canvas1.create_window(215, 432, anchor="nw", window=btnplay)
btnnew_canvas = canvas1.create_window(396, 432, anchor="nw", window=btnnew)
btnview_canvas = canvas1.create_window(580, 432, anchor="nw", window=btnview)
btnexit_canvas = canvas1.create_window(762, 432, anchor="nw", window=btnexit)

inichecker.inichecker()
# Execute tkinter
root.mainloop()
