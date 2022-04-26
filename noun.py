from tkinter import *
from tkinter.ttk import *
from pathlib import Path
import verb
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



def noun(tex):
    def savenoun(event="1"):
        texto = tex
        print("saved")
        no = entry.get()
        texto = texto.replace("NOUN", no, 1)
        entry.delete(0, END)
        askn.destroy()
        if "NOUN" in texto:
            noun(texto)
        elif "VERB" in texto:
            verb.verb(texto)
        elif "ADJECTIVE" in texto:
            adje.adje(texto)
        if "NOUN" not in texto and "VERB" not in texto and "ADJECTIVE" not in texto:
            showresult.result(texto)
            p = open(Path(f'{Path.home()}\\MadLips\\docs\\Your Tales.txt'), "a")
            p.write(f"\n{int(find_index.find_index())+1}- {texto}\n/")
            p.close()

    def closeaskn(event=None):
        askn.destroy()

    askn = Toplevel()
    askn.title("Enter a Noun")

    # Adjust size
    askn.geometry("913x473")

    #binding
    askn.bind("<Return>", savenoun)
    askn.bind("<Escape>", closeaskn)

    #images
    cancel_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\btncancel.png"))
    askn.cancel_img = cancel_img
    ok_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\btnok.png"))
    askn.ok_img = ok_img
    enternoun_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\enternoun.png"))
    askn.enternoun_img = enternoun_img

    # Create Canvas
    canvas1 = Canvas(askn, bg="#000fff030", bd=0, highlightthickness=0, width=913, height=473)
    canvas1.pack(fill="both", expand=True)
    # Display image
    canvas1.create_image(0, 0, image=askn.enternoun_img, anchor="nw")
    askn.wm_attributes("-transparentcolor", "#000fff030")

    # Create Buttons
    button1 = Button(askn, image=askn.ok_img, command=savenoun)
    button2 = Button(askn, image=askn.cancel_img, command=askn.destroy)
    entry = Entry(askn, font=("Times", "28", "bold italic"))

    # Display Buttons
    button1_canvas = canvas1.create_window(202, 327, anchor="nw", window=button1)
    button2_canvas = canvas1.create_window(517, 327, anchor="nw", window=button2)
    Entry_canvas = canvas1.create_window(250, 235, anchor="nw", window=entry)

    #focus
    entry.focus()
