from tkinter import *
from tkinter.ttk import *
from pathlib import Path
import adje
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
        # Just use file=resource_path('rock.png') instead of file='rock.png'
    return os.path.join(base_path, relative_path)


def verb(tex):
    def saveverb(event="1"):
        texto = tex
        print("saved")
        no = entry.get()
        texto = texto.replace("VERB", no, 1)
        entry.delete(0, END)
        askv.destroy()
        if "VERB" in texto:
            verb(texto)
        elif "ADJECTIVE" in texto:
            adje.adje(texto)
        if "NOUN" not in texto and "VERB" not in texto and "ADJECTIVE" not in texto:
            showresult.result(texto)
            p = open(Path(f'{Path.home()}\\MadLips\\docs\\Your Tales.txt'), "a")
            p.write(f"\n{int(find_index.find_index())+1}- {texto}\n/")
            p.close()


    def closeaskv(event=None):
        askv.destroy()

    askv = Toplevel()
    askv.title("Enter a Verb")
    # Adjust size
    askv.geometry("913x473")
    askv.bind("<Return>", saveverb)
    askv.bind("<Escape>", closeaskv)

    #images
    enterverb_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\enterverb.png"))
    askv.enterverb_img = enterverb_img
    cancel_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\btncancel.png"))
    askv.cancel_img = cancel_img
    ok_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\btnok.png"))
    askv.ok_img = ok_img

    # Create Canvas
    canvas1 = Canvas(askv, width=913, height=473, bg="#000fff030", bd=0, highlightthickness=0)
    canvas1.pack(fill="both", expand=True)
    # Display image
    canvas1.create_image(0, 0, image=askv.enterverb_img, anchor="nw")
    askv.wm_attributes("-transparentcolor", "#000fff030")

    # Create Buttons
    button1 = Button(askv, image=askv.ok_img, command=saveverb)
    button2 = Button(askv, image=askv.cancel_img, command=askv.destroy)
    entry = Entry(askv, font=("Times", "28", "bold italic"))

    # Display Buttons
    button1_canvas = canvas1.create_window(202, 327, anchor="nw", window=button1)

    button2_canvas = canvas1.create_window(517, 327, anchor="nw", window=button2)

    Entry_canvas = canvas1.create_window(250, 235, anchor="nw", window=entry)
    entry.focus()
