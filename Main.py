# Imports
from Caesar import *
from Tritheme import *
from Polybius import *
from Trifid import *
from A1Z26 import *
from Alphabetical_Substitution import *
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import filedialog


class StartFrame(Frame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        self.root = root

        # Buttons
        self.caesar_button = Button(self, text="Caesar", command=lambda: self.root.change_scene(
            CaesarFrame(root, 600)))
        self.caesar_button.config(width=15, fg='black', borderwidth=0, relief=RAISED)
        self.caesar_button.configure(highlightbackground='#27252c')
        self.caesar_button.place(relx=.5, rely=.14, anchor="center")

        self.tritheme_button = Button(self, text="Tritheme", command=lambda: self.root.change_scene(
            TrithemeFrame(root, 600)))
        self.tritheme_button.config(width=15, fg='black', borderwidth=0, relief=RAISED)
        self.tritheme_button.configure(highlightbackground='#27252c')
        self.tritheme_button.place(relx=.5, rely=.25, anchor="center")

        self.polybius_button = Button(self, text="Polybius", command=lambda: self.root.change_scene(
            PolybiusFrame(root, 600)))
        self.polybius_button.config(width=15, fg='black', borderwidth=0, relief=RAISED)
        self.polybius_button.configure(highlightbackground='#27252c')
        self.polybius_button.place(relx=.5, rely=.36, anchor="center")

        self.trifid_button = Button(self, text="Trifid", command=lambda: self.root.change_scene(
            TrifidFrame(root, 600)))
        self.trifid_button.config(width=15, fg='black', borderwidth=0, relief=RAISED)
        self.trifid_button.configure(highlightbackground='#27252c')
        self.trifid_button.place(relx=.5, rely=.47, anchor="center")

        self.a1z26_frame = Button(self, text="A1Z26", command=lambda: self.root.change_scene(
            A1Z26Frame(root, 600)))
        self.a1z26_frame.config(width=15, fg='black', borderwidth=0, relief=RAISED)
        self.a1z26_frame.configure(highlightbackground='#27252c')
        self.a1z26_frame.place(relx=.5, rely=.58, anchor="center")

        self.alphabetical_substitution_frame = Button(
            self, text="Alphabetical substitution", command=lambda: self.root.change_scene(
                AlphabeticalSubstitutionFrame(root, 600)))
        self.alphabetical_substitution_frame.config(width=15, fg='black', borderwidth=0, relief=RAISED)
        self.alphabetical_substitution_frame.configure(highlightbackground='#27252c')
        self.alphabetical_substitution_frame.place(relx=.5, rely=.69, anchor="center")

        self.experimental_frame = Button(self, text="Experimental function", command=lambda: self.root.change_scene(
            ExperimentalFrame(root, 600)))
        self.experimental_frame.config(width=15, fg='black', borderwidth=0, relief=RAISED)
        self.experimental_frame.configure(highlightbackground='#27252c')
        self.experimental_frame.place(relx=.5, rely=.80, anchor="center")

        """self.exit_button = Button(self, text="Exit", command=lambda: self.quit())
        self.exit_button.config(width=15, fg='black', borderwidth=0, relief=RAISED)
        self.exit_button.configure(highlightbackground='#27252c')
        self.exit_button.place(relx=.5, rely=.80, anchor="center")"""


class BaseFrame(Frame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        self.root = root

        # Labels
        self.choose_cipher = Label(self, text="Choose cipher", bg="#27252c")
        self.choose_cipher.place(x=30, y=50)
        self.plain_text = Label(self, text="Text", bg="#27252c")
        self.plain_text.place(x=30, y=90)
        self.choice = Label(self, text="Save encrypted text to txt file", bg="#27252c")
        self.choice.place(x=30, y=170)
        self.file_name = Label(self, text="Enter file name - leave blank if 'No' is selected", bg="#27252c")
        self.file_name.place(x=30, y=210)

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

        self.menu_button = Button(self, text="Back to menu", command=lambda: [self.root.change_scene(
            StartFrame(root, 600)), gui.title("Encrypt-decrypt app")])
        self.menu_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.menu_button.configure(highlightbackground='#27252c')
        self.menu_button.place(relx=.13, rely=.95, anchor="center")

    def save(self, final_text):
        if self.variable2.get() == self.choices[1]:
            file_name = self.file_name_input.get() + ".txt"
            with open(file_name, mode="w", encoding="utf-8") as file:
                file.write(final_text)

    def upload(self):
        path = filedialog.askopenfilename()

        if not path:
            messagebox.showinfo(title="FILE ERROR", message="No file selected!!!")
            return

        with open(path, mode="r", encoding="utf-8") as uploaded_file:
            uploaded_text = uploaded_file.read()
            self.plain_text_input.insert(END, uploaded_text)


class CaesarFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        gui.title("Caesar cipher")

        # Labels
        self.shift = Label(self, text="Shift", bg="#27252c")
        self.shift.place(x=30, y=130)

        # OptionMenus
        self.CIPHERS.append("Decrypt with all options")
        self.dropdown_menu['menu'].add_command(label="Decrypt with all options", command=tkinter._setit(
            self.variable, "Decrypt with all options"))

        self.shifts = []

        for x in range(25):
            self.shifts.append(x + 1)

        self.variable3 = StringVar(self)
        self.variable3.set(str(self.shifts[0]))

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
        self.submit_button.place(relx=.5, rely=.55, anchor="center")


class TrithemeFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        gui.title("Tritheme cipher")

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
        self.submit_button.place(relx=.5, rely=.55, anchor="center")


class PolybiusFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        gui.title("Polybius cipher")

        # Whats executed when submit button is clicked
        def action():

            if self.variable.get() == self.CIPHERS[0]:

                a = polybius_encrypt(self.plain_text_input.get())

                messagebox.showinfo(title="Encrypted text", message=a)
                PolybiusFrame.save(self, a)

            elif self.variable.get() == self.CIPHERS[1]:

                a = polybius_decrypt(self.plain_text_input.get())

                messagebox.showinfo(title="Decrypted text", message=a)
                PolybiusFrame.save(self, a)

        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.submit_button.configure(highlightbackground='#27252c')
        self.submit_button.place(relx=.5, rely=.55, anchor="center")


class TrifidFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        gui.title("Trifid cipher")

        # Labels
        self.shift = Label(self, text="Period", bg="#27252c")
        self.shift.place(x=310, y=130)
        self.key = Label(self, text="Key\n         (optional)", bg="#27252c")
        self.key.place(x=-4, y=130)

        # Inputs
        self.key_input = Entry(self)
        self.key_input.place(x=105, y=128)

        # OptionMenus
        self.period = []

        for x in range(16):
            self.period.append(x + 5)

        self.variable4 = StringVar(self)
        self.variable4.set(str(self.period[0]))

        self.dropdown_menu4 = OptionMenu(self, self.variable4, *self.period)
        self.dropdown_menu4.config(fg='black', borderwidth=0, relief=RAISED)
        self.dropdown_menu4.configure(highlightbackground='#27252c')
        self.dropdown_menu4.place(x=370, y=130)

        # Whats executed when submit button is clicked
        def action():

            if self.variable.get() == self.CIPHERS[0]:

                a = trifid_encrypt(self.plain_text_input.get(), int(self.variable4.get()), self.key_input.get())

                messagebox.showinfo(title="Encrypted text", message=a)
                TrifidFrame.save(self, a)

            elif self.variable.get() == self.CIPHERS[1]:

                a = trifid_decrypt(self.plain_text_input.get(), self.key_input.get())

                messagebox.showinfo(title="Decrypted text", message=a)
                TrifidFrame.save(self, a)

        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.submit_button.configure(highlightbackground='#27252c')
        self.submit_button.place(relx=.5, rely=.55, anchor="center")


class A1Z26Frame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        gui.title("A1Z26 cipher")

        # Labels
        self.separator = Label(self, text="Separator\n(optional)", bg="#27252c")
        self.separator.place(x=30, y=130)
        self.alphabet = Label(self, text="Alphabet\n(optional)", bg="#27252c")
        self.alphabet.place(x=300, y=130)

        # Inputs
        self.separator_input = Entry(self)
        self.separator_input.place(x=105, y=130)
        self.alphabet_input = Entry(self)
        self.alphabet_input.place(x=375, y=130)

        # Whats executed when submit button is clicked
        def action():

            if self.variable.get() == self.CIPHERS[0]:

                a = a1z26_encrypt(self.plain_text_input.get(), self.separator_input.get(), self.alphabet_input.get())

                messagebox.showinfo(title="Encrypted text", message=a)
                A1Z26Frame.save(self, a)

            elif self.variable.get() == self.CIPHERS[1]:

                a = a1z26_decrypt(self.plain_text_input.get(), self.separator_input.get(), self.alphabet_input.get())

                messagebox.showinfo(title="Decrypted text", message=a)
                A1Z26Frame.save(self, a)

        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.submit_button.configure(highlightbackground='#27252c')
        self.submit_button.place(relx=.5, rely=.55, anchor="center")


class AlphabeticalSubstitutionFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        gui.title("Alphabetical substitution")

        # Labels
        self.alphabet = Label(self, text="Alphabet\n(optional)", bg="#27252c")
        self.alphabet.place(x=30, y=130)
        self.ciphertext_alphabet = Label(self, text="Ciphertext\nalphabet\n(optional)", bg="#27252c")
        self.ciphertext_alphabet.place(x=300, y=130)

        # Inputs
        self.alphabet_input = Entry(self)
        self.alphabet_input.place(x=105, y=130)
        self.ciphertext_alphabet_input = Entry(self)
        self.ciphertext_alphabet_input.place(x=375, y=130)

        def action():

            if self.variable.get() == self.CIPHERS[0]:

                a = alphabetical_substitution_encrypt(self.plain_text_input.get(), self.alphabet_input.get(),
                                                      self.ciphertext_alphabet_input.get())

                messagebox.showinfo(title="Encrypted text", message=a)
                AlphabeticalSubstitutionFrame.save(self, a)

            elif self.variable.get() == self.CIPHERS[1]:

                a = alphabetical_substitution_decrypt(self.plain_text_input.get(), self.alphabet_input.get(),
                                                      self.ciphertext_alphabet_input.get())

                messagebox.showinfo(title="Decrypted text", message=a)
                AlphabeticalSubstitutionFrame.save(self, a)

        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.submit_button.configure(highlightbackground='#27252c')
        self.submit_button.place(relx=.5, rely=.55, anchor="center")


class ExperimentalFrame(BaseFrame):
    def __init__(self, root, height):
        super().__init__(root, height=height)
        gui.title("Experimental function")

        # Whats executed when submit button is clicked
        def action():
            try:
                print(polybius_decrypt(self.plain_text_input.get()))
            except Exception:
                try:
                    print(tritheme_decrypt(self.plain_text_input.get()))
                except Exception:
                    try:
                        print(polybius_decrypt(self.plain_text_input.get()))
                    except Exception:
                        return "Nebylo mozno desifrovat, pocet vyloucenych sifer: 3, vyloucene sifry: caesar, tritheme, polybius"

        # Buttons
        self.submit_button = Button(self, text="Submit", command=lambda: action())
        self.submit_button.config(width=10, fg='black', borderwidth=0, relief=RAISED)
        self.submit_button.configure(highlightbackground='#27252c')
        self.submit_button.place(relx=.5, rely=.55, anchor="center")


class GUI(Tk):
    def __init__(self, width, height, bgc, title):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.title(title)
        self.configure(bg=bgc)
        self.resizable(False, False)
        self.change_scene(StartFrame(self, 600))

        def show_info():
            messagebox.showinfo(title="About", message="© 2021 Zdenek Nemec")

        # Menu bar - About desc and Exit button
        self.menubar = Menu(self)
        self.appmenu = Menu(self.menubar, tearoff=0)
        self.appmenu.add_command(label="About", command=lambda: show_info())
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

# <3
