from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Listbox, END, messagebox, Toplevel
from MainUI import MainUI

def main():
    
    window = Tk()
    app = MainUI(window)
    window.resizable(False, False)
    window.mainloop()
if __name__ == "__main__":
    main()
    