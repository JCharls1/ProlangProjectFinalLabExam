from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Listbox, END, messagebox, Toplevel
import Parts
import PartsInventory
import Update

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ADMIN\Desktop\RefactoredProlang\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainUI:
    def __init__(self, root):
        self.parts_list = PartsInventory.PartsInventory()
        self.root = root
        self.root.geometry("700x500")
        self.root.configure(bg="#121212")
        self.currentNumber = 0
        
        self.canvas = Canvas(
            self.root,
            bg="#121212",
            height=500,
            width=700,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        self.setup_ui()
        
    def setup_ui(self):
        self.canvas.create_rectangle(
            0.0,
            0.0,
            700.0,
            98.0,
            fill="#6F2525",
            outline=""
        )

        self.canvas.create_text(
            13.0,
            22.0,
            anchor="nw",
            text=" Parts Inventory ",
            fill="#FFFFFF",
            font=("MontserratRoman Regular", 64 * -1)
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(229.5, 311.0, image=self.entry_image_1)
        self.description = Text(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.description.place(x=19.0, y=233.0, width=421.0, height=154.0)

        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(229.0, 162.0, image=self.entry_image_2)
        self.part_name = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.part_name.place(x=18.0, y=120.0, width=422.0, height=82.0)

        self.canvas.create_rectangle(456.0, 98.0, 700.0, 500.0, fill="#676565", outline="")
        self.canvas.create_rectangle(465.0, 117.0, 677.0, 184.0, fill="#666666", outline="")
        self.canvas.create_text(456.0, 106.0, anchor="nw", text="Parts", fill="#000000", font=("MontserratRoman Regular", 64 * -1))

        self.listbox = Listbox(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.listbox.place(x=465.0, y=182.0, width=230.0, height=308.0)

        self.listbox.bind("<<ListboxSelect>>", self.on_select)
        self.listbox.insert(END, "")
        
        self.listbox.bind("<Double-Button-1>", self.on_double_click)

        self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(99.0, 450.5, image=self.entry_image_4)
        self.price = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.price.place(x=18.0, y=415.0, width=162.0, height=69.0)

        self.canvas.create_text(203.0, 429.0, anchor="nw", text=" Add", fill="#000000", font=("MontserratRoman Regular", 24 * -1))
        self.canvas.create_text(280.0, 432.0, anchor="nw", text="Update", fill="#000000", font=("MontserratRoman Regular", 20 * -1))

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            text="Add",
            compound="center",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_item(),
            relief="flat"
        )
        self.button_1.place(x=198.0, y=429.0, width=62.0, height=32.0)

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.update_button = Button(
            image=self.button_image_2,
            text="Change",
            compound="center",
            borderwidth=0,
            highlightthickness=0,
            command=self.update_selected_item,  # Update the command to call check_selection
            relief="flat"
        )
        self.update_button.place(x=272.0, y=429.0, width=89.0, height=32.0)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            text="Delete",
            compound="center",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.delete_item(),
            relief="flat"
        )
        self.button_3.place(x=371.0, y=429.0, width=75.0, height=32.0)

        self.canvas.create_text(375.0, 433.0, anchor="nw", text="Delete", fill="#000000", font=("MontserratRoman Regular", 20 * -1))
        self.canvas.create_text(641.0, 80.0, anchor="nw", text="Admin ", fill="#FFFFFF", font=("MontserratRoman Regular", 16 * -1))
        self.canvas.create_text(18.0, 98.0, anchor="nw", text="Title", fill="#FFFFFF", font=("MontserratRoman Regular", 16 * -1))
        self.canvas.create_text(20.0, 211.0, anchor="nw", text="Description", fill="#FFFFFF", font=("MontserratRoman Regular", 16 * -1))
        self.canvas.create_text(20.0, 393.0, anchor="nw", text="Price", fill="#FFFFFF", font=("MontserratRoman Regular", 16 * -1))

    def on_double_click(self, event):
        selected_indices = self.listbox.curselection()
        self.part_name.delete(0, END)
        self.description.delete("1.0", "end")
        self.price.delete(0, END)
        if selected_indices:
            selected_item = self.listbox.get(selected_indices[0])
            print(f"Double-clicked item: {selected_item}")
            # Perform the desired action when an item is double-clicked
            self.part_name.insert(0, self.parts_list.Parts[int(selected_item[0])].part)
            self.description.insert("1.0", self.parts_list.Parts[int(selected_item[0])].description)
            self.price.insert(0, self.parts_list.Parts[int(selected_item[0])].price)
        else:
            print("No item selected")

    def on_select(self, event):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            selected_item = self.listbox.get(selected_indices[0])
            print(f"on_select: Selected item: {selected_item}")
        else:
            print("on_select: No item selected")

    def check_selection(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            print("check_selection: No item selected")
        else:
            selected_item = self.listbox.get(selected_indices[0])
            print(f"check_selection: Selected item: {selected_item}")
            
            num = int(selected_item.split(":")[0])
            print(num)
            Update.create_new_window(num, self.parts_list)
            part = Parts.Parts(Update.part, Update.desc, Update.price)
            self.parts_list.updatePart(part, num)
            
    def add_item(self):
        item = self.part_name.get()
        desc = self.description.get("1.0", "end-1c")
        price = self.price.get()
        if item:
            self.part_name.delete(0, END)
            self.description.delete("1.0", "end")
            self.price.delete(0, END)
            part = Parts.Parts(item, desc, price)
            self.parts_list.addPart(part, self.currentNumber)
            self.currentNumber += 1
            self.display_items()
        else:
            messagebox.showwarning("Input Error", "Please enter an item.")
        
    def delete_item(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            index = selected_indices[0]  # Get the index of the selected item
            selected_item = self.listbox.get(index)  # Get the text of the selected item
            parts_number = int(selected_item.split(":")[0])  # Extract the parts number from the text
            
            # Remove the item from the listbox
            self.listbox.delete(index)
            
            # Delete the corresponding item from self.parts_list.Parts
            del self.parts_list.Parts[parts_number]
            del self.parts_list.numbers[parts_number]

            
            print("Item deleted successfully.")
            for parts in self.parts_list.numbers:
                print(parts)
                print(self.parts_list.Parts[parts].part)
        
        else:
            print("No item selected to delete.")
    
    def update_selected_item(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            print("update_selected_item: No item selected")
        else:
            index = selected_indices[0]
            selected_item = self.listbox.get(index)
            print(f"update_selected_item: Selected item: {selected_item}")
            # Extract the data from the entry widgets
            new_part_name = self.part_name.get()
            new_description = self.description.get("1.0", END).strip()
            new_price = self.price.get()
            # Create the updated text for the selected item
            updated_text = f"{index}: {new_part_name}"
            # Update the selected item in the Listbox
            self.listbox.delete(index)
            self.listbox.insert(index, updated_text)
            # Update the corresponding item in self.parts_list.Parts
            self.parts_list.Parts[index] = Parts.Parts(new_part_name, new_description, new_price)
            print("Item updated successfully.")    

    def display_items(self):
        self.clear_listbox()
        for parts in self.parts_list.numbers:
            print(parts)
            print(self.parts_list.Parts[parts].part)
            text = f"{str(parts)}: {self.parts_list.Parts[parts].part}"
            self.listbox.insert(END, text)
            

    def clear_listbox(self, event=None):
        self.listbox.delete(0, END)
    