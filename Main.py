# Imports
from Caesar import *
from tkinter import *
from tkinter import messagebox


class StartFrame(Frame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        self.root = root

        # Buttons
        Button(self, text="Caesar", command=lambda: self.root.change_scene(
            CaesarFrame(root, 600))).place(relx=.5, rely=.04, anchor="c")
        Button(self, text="Base", command=lambda: self.root.change_scene(
            BaseFrame(root, 600))).place(relx=.5, rely=.09, anchor="c")


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
        self.CIPHERS = ["Encrypt", "Decrypt", "Decrypt with all options"]
        self.choices = ["No", "Yes"]

        self.variable = StringVar(self)
        self.variable.set(self.CIPHERS[0])

        self.variable2 = StringVar(self)
        self.variable2.set(self.choices[0])

        self.dropdown_menu = OptionMenu(self, self.variable, *self.CIPHERS)
        self.dropdown_menu.place(x=160, y=50)

        self.dropdown_menu2 = OptionMenu(self, self.variable2, *self.choices)
        self.dropdown_menu2.place(x=229, y=170)

    def save(self, final_text):
        if self.variable2.get() == self.choices[1]:
            file_name = self.file_name_input.get() + ".txt"
            with open(file_name, mode="w", encoding="utf-8") as file:
                file.write(final_text)


class CaesarFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)

        # Labels
        self.shift = Label(self, text="Shift").place(x=30, y=130)

        # OptionMenus
        self.shifts = []

        for x in range(25):
            self.shifts.append(x + 1)

        self.variable3 = StringVar(self)
        self.variable3.set(self.shifts[0])

        self.dropdown_menu3 = OptionMenu(self, self.variable3, *self.shifts)
        self.dropdown_menu3.place(x=105, y=130)

        # Whats executed when submit button is clicked
        def action():  # Edit action efficiency, make 'a' variable for whole function and make one try except

            if self.variable.get() == self.CIPHERS[0]:

                a = caesar_encrypt(self.plain_text_input.get(), int(self.variable3.get()))
                messagebox.showinfo(title="Encrypted text", message=a)
                CaesarFrame.save(self, a)

            elif self.variable.get() == self.CIPHERS[1]:

                a = caesar_decrypt(self.plain_text_input.get())
                messagebox.showinfo(title="Decrypted text", message=a)
                CaesarFrame.save(self, a)

            elif self.variable.get() == self.CIPHERS[2]:

                a = caesar_manual_decrypt(self.plain_text_input.get())
                afinal = ""

                for word in a:
                    afinal += word
                    afinal += 3*"\n"

                messagebox.showinfo(title="Decrypted text", message=afinal)
                CaesarFrame.save(self, afinal)

        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.place(relx=.5, rely=.55, anchor="c")


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

    def change_scene(self, frame_class):
        self.frame = frame_class
        self.frame.grid(row=0, column=0, sticky="ew")
        self.frame.configure(bg="#27252c")
        self.frame.tkraise()


gui = GUI(600, 600, "#27252c", "Encrypt-decrypt app")
gui.grid_columnconfigure(0, weight=1)
gui.mainloop()
