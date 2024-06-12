
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Listbox, END, messagebox, Toplevel
from pathlib import Path
import Parts

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ADMIN\Desktop\RefactoredProlang\build\assets1\frame0")
part = ""
desc = ""
price = ""

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def create_new_window(num, list):
    new_window = Toplevel()
    new_window.geometry("700x500")
    new_window.configure(bg="#C3C3C3")

    canvas = Canvas(
        new_window,
        bg="#C3C3C3",
        height=500,
        width=700,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        62.0,
        fill="#FDFD96",
        outline=""
    )
    canvas.create_text(
        0.0,
        0.0,
        anchor="nw",
        text="Update",
        fill="#000000",
        font=("Inter", 48 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        350.0,
        123.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        new_window,  # Specify the parent as the new window
        bd=0,
        bg="#F1F1F1",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=183.0,
        y=89.0,
        width=334.0,
        height=66.0
    )

    # Add other widgets here...
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        350.0,
        286.5,
        image=entry_image_2
    )
    entry_2 = Text(
        new_window,
        bd=0,
        bg="#F1F1F1",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=123.0,
        y=184.0,
        width=454.0,
        height=203.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        261.5,
        435.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        new_window,
        bd=0,
        bg="#F1F1F1",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=183.0,
        y=410.0,
        width=157.0,
        height=48.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        new_window,
        image=button_image_1,
        text = "Update",
        compound="center",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setUpdate(entry_1.get(), entry_2.get("1.0", "end-1c"), entry_3.get(), num),
        relief="flat"
    )
    button_1.place(
        x=360.0,
        y=410.0,
        width=157.0,
        height=50.0
    )
    
    

    canvas.create_text(
        183.0,
        64.0,
        anchor="nw",
        text="Part",
        fill="#000000",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        123.0,
        157.0,
        anchor="nw",
        text="Description",
        fill="#000000",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        181.0,
        389.0,
        anchor="nw",
        text="Price",
        fill="#000000",
        font=("Inter", 20 * -1)
    )

    new_window.mainloop()
    
def setUpdate(Part, Desc, Price, num):
    part = Part
    desc = Desc
    price = Price

def getUpdate():
    return [part, desc, price]