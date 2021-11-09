# Imports
import tkinter.messagebox

from Caesar import *
from tkinter import *
from tkinter import messagebox


class StartFrame(Frame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        self.root = root
        Button(self, text="Caesar", command=lambda: self.root.change_scene(
            CaesarFrame(root, 600))).grid(row=1, column=0)


class BaseFrame(Frame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        self.root = root

        # Labels
        self.choose_cipher = Label(self, text="Choose cipher").place(x=30, y=50)
        self.plain_text = Label(self, text="Text").place(x=30, y=90)
        self.choice = Label(self, text="Save encrypted text to txt file").place(x=30, y=170)
        self.file_name = Label(self, text="Enter file name - leave blank if 'No' is selected").place(x=30, y=210)

        # Inputs
        self.plain_text_input = Entry(self)
        self.plain_text_input.place(x=105, y=90)
        self.file_name_input = Entry(self)
        self.file_name_input.place(x=30, y=250)

        # OptionMenus
        self.CIPHERS = ["Encrypt", "Decrypt"]
        self.choices = ["No", "Yes"]

        self.variable = StringVar(self)
        self.variable.set(self.CIPHERS[0])

        self.variable2 = StringVar(self)
        self.variable2.set(self.choices[0])

        self.dropdown_menu = OptionMenu(self, self.variable, *self.CIPHERS)
        self.dropdown_menu.place(x=160, y=50)

        self.dropdown_menu2 = OptionMenu(self, self.variable2, *self.choices)
        self.dropdown_menu2.place(x=229, y=170)


class CaesarFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)

        # Labels
        self.shift = Label(self, text="Shift").place(x=30, y=130)

        # Inputs

        # OptionMenus
        self.shifts = []

        for x in range(25):
            self.shifts.append(x + 1)

        self.variable3 = StringVar(self)
        self.variable3.set(self.shifts[0])

        self.dropdown_menu3 = OptionMenu(self, self.variable3, *self.shifts)
        self.dropdown_menu3.place(x=105, y=130)

        # Whats executed when submit button is clicked
        def action():

            if self.variable.get() == self.CIPHERS[0]:

                a = caesar_encrypt(self.plain_text_input.get(), int(self.variable3.get()))

                try:
                    self.encrypted.destroy()
                except:
                    pass

                try:
                    self.decrypted.destroy()
                except:
                    pass

                self.encrypted = Label(self, text="Encrypted text: " + a)
                self.encrypted.place(relx=.5, rely=.65, anchor="c")

                if self.variable2.get() == self.choices[1]:
                    self.file_name = self.file_name_input.get() + ".txt"
                    with open(self.file_name, mode="w", encoding="utf-8") as file:
                        file.write(a)

            elif self.variable.get() == self.CIPHERS[1]:

                a = caesar_decrypt(self.plain_text_input.get())

                try:
                    self.encrypted.destroy()
                except:
                    pass

                try:
                    self.decrypted.destroy()
                except:
                    pass

                self.decrypted = Label(self, text="Decrypted text: " + a)
                self.decrypted.place(relx=.5, rely=.65, anchor="c")

                if self.variable2.get() == self.choices[1]:
                    self.file_name = self.file_name_input.get() + ".txt"
                    with open(self.file_name, mode="w", encoding="utf-8") as file:
                        file.write(a)

        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.place(x=260, y=330)

        def onclick():
            tkinter.messagebox.showinfo("Full list", caesar_manual_decrypt(self.plain_text_input.get()))

        self.buton = Button(self, text="click", command=onclick)
        self.buton.place(x=260, y=400)


"""def change_scene(frame_class):
    frame = frame_class
    frame.grid(row=0, column=0, sticky="ew")
    frame.configure(bg="#27252c")
    frame.tkraise()"""


class GUI(Tk):
    def __init__(self, width, height, bgc, title):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.title(title)
        self.configure(bg=bgc)
        self.resizable(False, False)
        self.change_scene(StartFrame(self, 600))

        # Menu bar - About desc and Exit button
        self.menubar = Menu(self)
        self.appmenu = Menu(self.menubar, tearoff=0)
        self.appmenu.add_command(label="About")
        self.appmenu.add_separator()
        self.appmenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="Application", menu=self.appmenu)
        self.configure(menu=self.menubar)

        # Scene changing buttons
        """self.caesar_button = Button(self, text="Caesar cipher", command=lambda: change_scene(
            CaesarFrame(self, 600))).grid(row=1, column=0)
        self.random_button = Button(self, text="Random cipher", command=lambda: change_scene(
            BaseFrame(self, 600))).grid(row=2, column=0)"""

    def change_scene(self, frame_class):
        self.frame = frame_class
        self.frame.grid(row=0, column=0, sticky="ew")
        self.frame.configure(bg="#27252c")
        self.frame.tkraise()


gui = GUI(600, 600, "#27252c", "Encrypt-decrypt app")
gui.grid_columnconfigure(0, weight=1)
gui.mainloop()
