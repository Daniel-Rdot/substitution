#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class Substitution2App:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.title("Oxydierer")
        self.toplevel1.configure(height=200, width=200)
        self.encrypt = ttk.Button(self.toplevel1)
        self.mode_encrypt = tk.StringVar(value='encrypt')
        self.encrypt.configure(
            text='encrypt',
            textvariable=self.mode_encrypt,
            width=20)
        self.encrypt.grid(column=1, columnspan=2, padx=5, row=1)
        self.encrypt.configure(command=self.press_encrypt)
        self.decrypt = ttk.Button(self.toplevel1)
        self.mode_decrypt = tk.StringVar(value='decrypt')
        self.decrypt.configure(
            text='decrypt',
            textvariable=self.mode_decrypt,
            width=20)
        self.decrypt.grid(column=1, columnspan=2, padx=5, row=2)
        self.decrypt.configure(command=self.press_decrypt)
        self.key_input = ttk.Entry(self.toplevel1)
        self.key = tk.StringVar(value='... Hier Key eingeben')
        self.key_input.configure(
            justify="right",
            show='*',
            textvariable=self.key,
            width=30)
        _text_ = '...Hier Key eingeben'
        self.key_input.delete("0", "end")
        self.key_input.insert("0", _text_)
        self.key_input.grid(column=1, padx=5, row=0)
        self.text_input = tk.Text(self.toplevel1)
        self.text_input.configure(
            blockcursor="false",
            height=15,
            takefocus=True,
            undo="true",
            bg = "light yellow",
            width=50)
        self.text_input.grid(column=0, padx=10, pady=10, row=0, rowspan=3)
        self.text_output = tk.Text(self.toplevel1)
        self.text_output.configure(
            height=15,
            setgrid="false",
            state="normal",
            bg = "light cyan",
            width=50)
        self.text_output.grid(column=3, row=0, rowspan=3)
        self.toplevel1.grid_anchor("n")
        self.toplevel1.rowconfigure("all", minsize=50)
        self.toplevel1.columnconfigure("all", minsize=50)
        self.clear = ttk.Button(self.toplevel1)
        self.clear.configure(text='clear')
        self.clear.grid(column=0, row=3, sticky="n")
        self.clear.configure(command=self.press_clear)
        self.copy = ttk.Button(self.toplevel1)
        self.copy_text = tk.StringVar(value='copy')
        self.copy.configure(text='copy', textvariable=self.copy_text)
        self.copy.grid(column=3, row=3, sticky="n")
        self.copy.configure(command=self.press_copy)
        self.toplevel1.grid_anchor("n")
        self.toplevel1.rowconfigure("all", minsize=50)
        self.toplevel1.columnconfigure("all", minsize=50)
        self.button1 = ttk.Button(self.toplevel1)
        self.oxy_history = tk.StringVar(value='history')
        self.historydict = {}
        self.button1.configure(text='history', textvariable=self.oxy_history)
        self.button1.grid(column=1, row=3, sticky="n")
        self.button1.configure(command=self.press_history)
        self.toplevel1.grid_anchor("n")
        self.toplevel1.rowconfigure("all", minsize=50)
        self.toplevel1.columnconfigure("all", minsize=50)
        self.button1.configure(text='history', textvariable=self.oxy_history)
        self.button1.grid(column=1, columnspan=2, row=3, sticky="n")
        self.button1.configure(command=self.press_history)
        self.show_password = ttk.Button(self.toplevel1)
        self.show_password.configure(text='Show Password')
        self.show_password.grid(column=2, row=0)
        self.show_password.configure(command=self.toggle_password)
        self.toplevel1.grid_anchor("n")
        self.toplevel1.rowconfigure("all", minsize=50)
        self.toplevel1.columnconfigure("all", minsize=50)


        # Main widget
        self.mainwindow = self.toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def press_encrypt(self):
        pass

    def press_decrypt(self):
        pass

    def press_clear(self):
        pass

    def press_copy(self):
        pass

    def press_history(self):
        pass

    def toggle_password(self):
        pass
    
if __name__ == "__main__":
    app = Substitution2App()
    app.run()
