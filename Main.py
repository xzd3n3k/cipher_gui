# Imports
from Caesar import *
from tkinter import *

"""
# Root window settings
root = Tk()
root.geometry("600x600")
root.title("Encrypt-decrypt")
root.resizable(False, False)

# Labels
choose_cipher = Label(root, text="Choose cipher").place(x=30, y=50)
plain_text = Label(root, text="Text").place(x=30, y=90)
shift = Label(root, text="Shift").place(x=30, y=130)
choice = Label(root, text="Save encrypted text to txt file").place(x=30, y=170)
file_name = Label(root, text="Enter file name - leave blank if 'No' is selected").place(x=30, y=210)

# Inputs
plain_text_input = Entry(root)
plain_text_input.place(x=105, y=90)
# shift_input = Entry(root).place(x=105, y=130)
file_name_input = Entry(root)
file_name_input.place(x=30, y=250)

# OptionMenus
shifts = []
for x in range(25):
    shifts.append(x + 1)

CIPHERS = ["Encrypt", "Decrypt"]
choices = ["No", "Yes"]

variable = StringVar(root)
variable.set(CIPHERS[0])

variable2 = StringVar(root)
variable2.set(choices[0])

variable3 = StringVar(root)
variable3.set(shifts[0])

dropdown_menu = OptionMenu(root, variable, *CIPHERS)
dropdown_menu.place(x=160, y=50)

dropdown_menu2 = OptionMenu(root, variable2, *choices)
dropdown_menu2.place(x=229, y=170)

dropdown_menu3 = OptionMenu(root, variable3, *shifts)
dropdown_menu3.place(x=105, y=130)


# Whats executed when submit button is clicked
def action():
    global plain_text_input
    global variable3
    print(variable3)
    print(plain_text_input)
    if variable.get() == CIPHERS[0]:
        caesar_encrypt(plain_text_input.get(), int(variable3.get()))
    elif variable.get() == CIPHERS[1]:
        caesar_decrypt()


# Buttons
submit_button = Button(root, text="Submit", command=lambda: action())
submit_button.place(x=260, y=330)

# Menubar settings
menubar = Menu(root)
appmenu = Menu(menubar, tearoff=0)
appmenu.add_command(label="About")
appmenu.add_separator()
appmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Application", menu=appmenu)
root.configure(menu=menubar, bg="#27252c")

root.mainloop()"""


class BaseFrame(Frame):
    def __init__(self, root, name, height):
        super().__init__(root, height=height)
        self.root = root
        self.title = Label(self, text=name)


class CaesarFrame(BaseFrame):
    def __init__(self, root, name, height):
        super().__init__(root, name, height=height)
        self.shift_label = Label(self, text="Shift: ")
        self.shift_entry = Entry(self)
        self.shift_label.pack()
        self.shift_entry.pack()


class GUI(Tk):
    def __init__(self, width, height, bgc, title):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.title(title)
        self.configure(bg=bgc)
        self.resizable(False, False)

        self.menubar = Menu(self)
        self.appmenu = Menu(self.menubar, tearoff=0)
        self.appmenu.add_command(label="About")
        self.appmenu.add_separator()
        self.appmenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="Application", menu=self.appmenu)
        self.configure(menu=self.menubar)

        self.ciphers = {"Random cipher": BaseFrame(self, "base", 600), "Caesar cipher": CaesarFrame(self, "caesar", 600)}

        for i, (cipher_name, cipher_frame) in enumerate(self.ciphers.items()):
            Button(self, text=cipher_name, command=lambda: self.change_scene(cipher_name, cipher_frame)).grid(row=i, column=0)
            print(cipher_name, cipher_frame)

    def change_scene(self, name, frame_class):
        frame = frame_class
        frame.grid(row=0, column=0, sticky="ew")
        frame.tkraise()
        print(frame)


gui = GUI(600, 600, "#27252c", "Encrypt-decrypt")
gui.grid_columnconfigure(0, weight=1)
gui.mainloop()
