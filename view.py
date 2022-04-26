from tkinter import *
from tkinter.ttk import *
from pathlib import Path
import find_index
import showresult
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




def view():
    def show(event=None):
        # Finding the tale
        selected = clicked.get()
        single = ""
        tales = Path(f'{Path.home()}\\MadLips\\docs\\Your Tales.txt').read_text()

        for i in tales:
            if i != "/":
                single = single + i
            else:
                if single[1 : (len(selected)) + 2] == str(selected)+'-':
                    showresult.result(single)
                    single = ""
                else:
                    single = ""



    def closeview(event=None):
        view_wind.destroy()

    view_wind = Toplevel()
    view_wind.title("Visiting your old tales")
    view_wind.iconbitmap("C:/Users/natas/Downloads/Radiation.ico")
    view_wind.geometry("913x473")

    # binding return and escape
    view_wind.bind("<Return>", show)
    view_wind.bind("<Escape>", closeview)

    # Images
    view_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\view.png"))
    view_wind.view_img = view_img
    askview_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\askview.png"))
    view_wind.askview_img = askview_img
    cancel_img = PhotoImage(file=resource_path(f"{Path.home()}\\MadLips\\btncancel.png"))
    view_wind.cancel_img = cancel_img

    # Creating canvas
    canvas1 = Canvas(view_wind, width=913, height=473, bg="#000fff030", bd=0, highlightthickness=0)
    view_wind.wm_attributes("-transparentcolor", "#000fff030")
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=view_wind.askview_img, anchor="nw")

    # Creating Button
    view_btn = Button(view_wind, image=view_wind.view_img, command=show)
    cancel_btn = Button(view_wind, image=view_wind.cancel_img, command=closeview)
    # Display Button
    button_view_canvas = canvas1.create_window(202, 327, anchor="nw", window=view_btn)
    button_cancel_canvas = canvas1.create_window(517, 327, anchor="nw", window=cancel_btn)

    # Showing options
    index = find_index.find_index()
    options = []
    for n in range(1,(int(index)+1)):
        options.append(n)
    clicked = StringVar()
    drop = OptionMenu(view_wind, clicked, options[0], *options)
    drop_canvas = canvas1.create_window(425, 65, anchor='nw', window=drop)
