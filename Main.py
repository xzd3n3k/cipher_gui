# Imports
from Caesar import *
from Tritheme import *
from Polybius import *
from Trifid import *
from tkinter import *
from tkinter import messagebox, _setit
from tkinter import filedialog


class StartFrame(Frame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        self.root = root

        # Buttons
        self.caesar_button = Button(self, text="Caesar", command=lambda: self.root.change_scene(
            CaesarFrame(root, 600)))
        self.caesar_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.caesar_button.configure(highlightbackground='#27252c')
        self.caesar_button.place(relx=.5, rely=.04, anchor="c")

        self.tritheme_button = Button(self, text="Tritheme", command=lambda: self.root.change_scene(
            TrithemeFrame(root, 600)))
        self.tritheme_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.tritheme_button.configure(highlightbackground='#27252c')
        self.tritheme_button.place(relx=.5, rely=.09, anchor="c")

        self.polybius_button = Button(self, text="Polybius", command=lambda: self.root.change_scene(
            PolybiusFrame(root, 600)))
        self.polybius_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.polybius_button.configure(highlightbackground='#27252c')
        self.polybius_button.place(relx=.5, rely=.14, anchor="c")

        self.base_button = Button(self, text="Base", command=lambda: self.root.change_scene(
            BaseFrame(root, 600)))
        self.base_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.base_button.configure(highlightbackground='#27252c')
        self.base_button.place(relx=.5, rely=.19, anchor="c")

        self.exit_button = Button(self, text="Exit", command=lambda: self.quit())
        self.exit_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.exit_button.configure(highlightbackground='#27252c')
        self.exit_button.place(relx=.5, rely=.24, anchor="c")


class BaseFrame(Frame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        self.root = root

        # Labels
        self.choose_cipher = Label(self, text="Choose cipher", bg="#27252c").place(x=30, y=50)
        self.plain_text = Label(self, text="Text", bg="#27252c").place(x=30, y=90)
        self.choice = Label(self, text="Save encrypted text to txt file", bg="#27252c").place(x=30, y=170)
        self.file_name = Label(self, text="Enter file name - leave blank if 'No' is selected",
                               bg="#27252c").place(x=30, y=210)

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
        self.dropdown_menu.config(fg='black', borderwidth=0, relief=RAISED)
        self.dropdown_menu.configure(highlightbackground='#27252c')
        self.dropdown_menu.place(x=160, y=50)

        self.dropdown_menu2 = OptionMenu(self, self.variable2, *self.choices)
        self.dropdown_menu2.config(fg='black', borderwidth=0, relief=RAISED)
        self.dropdown_menu2.configure(highlightbackground='#27252c')
        self.dropdown_menu2.place(x=229, y=170)

        # Buttons
        self.upload_button = Button(self, text="Upload", command=lambda: self.upload())
        self.upload_button.config(fg='black', borderwidth=0, relief=RAISED)
        self.upload_button.configure(highlightbackground='#27252c')
        self.upload_button.place(x=310, y=90)

        self.menu_button = Button(self, text="Back to menu", command=lambda: self.root.change_scene(
            StartFrame(root, 600)))
        self.menu_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.menu_button.configure(highlightbackground='#27252c')
        self.menu_button.place(relx=.13, rely=.95, anchor="c")

    def save(self, final_text):
        if self.variable2.get() == self.choices[1]:
            file_name = self.file_name_input.get() + ".txt"
            with open(file_name, mode="w", encoding="utf-8") as file:
                file.write(final_text)

    def upload(self):
        path = filedialog.askopenfilename()
        print(path)


class CaesarFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)

        # Labels
        self.shift = Label(self, text="Shift", bg="#27252c").place(x=30, y=130)

        # OptionMenus
        self.CIPHERS.append("Decrypt with all options")
        self.dropdown_menu['menu'].add_command(label="Decrypt with all options", command=_setit(
            self.variable, "Decrypt with all options"))

        self.shifts = []

        for x in range(25):
            self.shifts.append(x + 1)

        self.variable3 = StringVar(self)
        self.variable3.set(self.shifts[0])

        self.dropdown_menu3 = OptionMenu(self, self.variable3, *self.shifts)
        self.dropdown_menu3.config(fg='black', borderwidth=0, relief=RAISED)
        self.dropdown_menu3.configure(highlightbackground='#27252c')
        self.dropdown_menu3.place(x=105, y=130)

        # Whats executed when submit button is clicked
        def action():

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
                a_final = ""

                for word in a:
                    a_final += word
                    a_final += 3 * "\n"

                messagebox.showinfo(title="Decrypted text", message=a_final)
                CaesarFrame.save(self, a_final)

        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.submit_button.configure(highlightbackground='#27252c')
        self.submit_button.place(relx=.5, rely=.55, anchor="c")


class TrithemeFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)

        # Whats executed when submit button is clicked
        def action():

            if self.variable.get() == self.CIPHERS[0]:

                a = tritheme_encrypt(self.plain_text_input.get())

                messagebox.showinfo(title="Encrypted text", message=a)
                TrithemeFrame.save(self, a)

            elif self.variable.get() == self.CIPHERS[1]:

                a = tritheme_decrypt(self.plain_text_input.get())

                messagebox.showinfo(title="Decrypted text", message=a)
                TrithemeFrame.save(self, a)
        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.submit_button.configure(highlightbackground='#27252c')
        self.submit_button.place(relx=.5, rely=.55, anchor="c")


class PolybiusFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)

        # Whats executed when submit button is clicked
        def action():

            if self.variable.get() == self.CIPHERS[0]:

                a = polybius_encrypt(self.plain_text_input.get())

                messagebox.showinfo(title="Encrypted text", message=a)
                TrithemeFrame.save(self, a)

            elif self.variable.get() == self.CIPHERS[1]:

                a = polybius_decrypt(self.plain_text_input.get())

                messagebox.showinfo(title="Decrypted text", message=a)
                TrithemeFrame.save(self, a)

        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.submit_button.configure(highlightbackground='#27252c')
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
