from tkinter import *
from tkinter.ttk import *
import os, random, string
from pathlib import Path
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



def register():
    def savemod(event=None):
        print("saved")
        random20 = "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(20)
        )
        newmad = Path(f'{Path.home()}\\MadLips\\docs\\{random20}.txt')
        model = entry.get()
        newmad.write_text(model)
        regist_wind.destroy()

    def closenewm(event=None):
        regist_wind.destroy()


    regist_wind = Toplevel()
    regist_wind.title("Registering New Model")
    regist_wind.geometry("913x473")
    # binding return and escape
    regist_wind.bind("<Return>", savemod)
    regist_wind.bind("<Escape>", closenewm)


    savemodel_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\savemodel.png"))
    regist_wind.savemodel_img = savemodel_img
    cancelmodel_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\cancelmodel.png"))
    regist_wind.cancelmodel_img = cancelmodel_img
    newstory_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\enternewstory.png"))
    regist_wind.newstory_img = newstory_img
    # Create Canvas
    canvas1 = Canvas(regist_wind, width=913, height=473, bg="#000fff030", bd=0, highlightthickness=0)
    canvas1.pack(fill="both", expand=True)
    regist_wind.wm_attributes("-transparentcolor", "#000fff030")
    # Display image
    canvas1.create_image(0, 0, image=regist_wind.newstory_img, anchor="nw")
    # Create Buttons
    btn_save_newstory = Button(regist_wind, image=regist_wind.savemodel_img, command=savemod)
    btn_cancel_newstory = Button(
        regist_wind, image=regist_wind.cancelmodel_img, command=regist_wind.destroy
    )
    entry = Entry(regist_wind, font=("Times", "18", "bold italic"), width=65)
    # Display Buttons
    button1_canvas = canvas1.create_window(
        202, 327, anchor="nw", window=btn_save_newstory
    )
    button2_canvas = canvas1.create_window(
        517, 327, anchor="nw", window=btn_cancel_newstory
    )
    Entry_canvas = canvas1.create_window(50, 265, anchor="nw", window=entry)
    entry.focus()
