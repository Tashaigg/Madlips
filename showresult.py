from tkinter import *
from tkinter.ttk import *
from pathlib import Path


def result(tex='The text would be showed here.'):

    def closeres(event=None):
        result_wind.destroy()

    result_wind = Toplevel()
    result_wind.title("Your Story")
    # Adjust size
    result_wind.geometry("1300x740")
    # binding
    result_wind.bind("<Return>", closeres)
    result_wind.bind("<Escape>", closeres)


    ok_image = PhotoImage(file=f"{Path.home()}\\MadLips\\btnok.png")
    bill_image = PhotoImage(file=f"{Path.home()}\\MadLips\\bill.png")
    result_wind.ok_img = ok_image
    result_wind.bill_img = bill_image

    # Create Canvas
    canvas1 = Canvas(result_wind, width=913, height=473)
    canvas1.pack(fill="both", expand=True)
    # Display image
    canvas1.create_image(0, 0, image=result_wind.bill_img, anchor="nw")
    canvas1.create_text(
        720,
        180,
        text=tex,
        angle=9,
        width=780,
        font=("Times", "28", "bold italic"),
    )
    # Create Buttons
    btn_close = Button(result_wind, image=result_wind.ok_img, command=result_wind.destroy)

    # Display Buttons
    btn_close_canvas = canvas1.create_window(1002, 527, anchor="nw", window=btn_close)
    btn_close.focus()


if __name__ == "__main__":
    root = Tk()
    label1 = Label(root, text= 'Test for result window')
    label1.pack()
    Button(root, text="open result window", command=result).pack()
    root.mainloop()
