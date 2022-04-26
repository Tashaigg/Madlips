from tkinter import *
from tkinter.ttk import *
from pathlib import Path
import showresult
import find_index
import sys, os
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        # Just use file=resource_path('image.png') instead of file='image.png'
    return os.path.join(base_path, relative_path)


def adje(tex):
    def saveadje(event="1"):
        texto = tex
        print("saved")
        no = entry.get()
        texto = texto.replace("ADJECTIVE", no, 1)
        entry.delete(0, END)
        aska.destroy()
        if "ADJECTIVE" in texto:
            adje(texto)
        if "NOUN" not in texto and "VERB" not in texto and "ADJECTIVE" not in texto:
            showresult.result(texto)
            p = open(Path('docs\\Your Tales.txt'), "a")
            p.write(f"\n{int(find_index.find_index())+1}- {texto}\n/")
            p.close()

    def closeaska(event=None):
        aska.destroy()

    aska = Toplevel()
    aska.title("Enter a Adjective")
    # Adjust size
    aska.geometry("913x473")
    aska.bind("<Return>", saveadje)
    aska.bind("<Escape>", closeaska)

    #images
    cancel_img = PhotoImage(file=resource_path('btncancel.png'))
    aska.cancel_img = cancel_img
    ok_img = PhotoImage(file=resource_path('btnok.png'))
    aska.ok_img = ok_img
    enteradjective_img = PhotoImage(file=resource_path(f"enteradjective.png"))
    aska.enteradjective_img = enteradjective_img

    # Create Canvas
    canvas1 = Canvas(aska, width=913, height=473, bg="#000fff030", bd=0, highlightthickness=0)
    canvas1.pack(fill="both", expand=True)
    # Display image
    canvas1.create_image(0, 0, image=aska.enteradjective_img, anchor="nw")
    aska.wm_attributes("-transparentcolor", "#000fff030")

    # Create Buttons
    button1 = Button(aska, image=aska.ok_img, command=saveadje)
    button2 = Button(aska, image=aska.cancel_img, command=aska.destroy)
    entry = Entry(aska, font=("Times", "28", "bold italic"))

    # Display Buttons
    button1_canvas = canvas1.create_window(202, 327, anchor="nw", window=button1)

    button2_canvas = canvas1.create_window(517, 327, anchor="nw", window=button2)

    Entry_canvas = canvas1.create_window(250, 235, anchor="nw", window=entry)
    entry.focus()
