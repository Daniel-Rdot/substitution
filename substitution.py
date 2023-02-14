import tkinter as tk
import tkinter.ttk as ttk
from substitution_gui import Substitution2App
from oxydierer import oxy_encrypt, oxy_decrypt
import json
import webbrowser

class Oxydierer(Substitution2App):
    def __init__(self, master=None):
        Substitution2App.__init__(self, master)



    def press_encrypt(self):
        txt_input = self.text_input.get("1.0", "end-1c")
        if self.text_output.get("1.0", "end-1c") != "":
            self.text_output.delete("1.0", tk.END)
        after = oxy_encrypt(txt_input, self.key.get())
        self.text_output.insert(tk.END, after)
        self.historydict.update({txt_input: after})

    def press_decrypt(self):
        txt_input = self.text_input.get("1.0", "end-1c")
        if self.text_output.get("1.0", "end-1c") != "":
            self.text_output.delete("1.0", tk.END)
        after = oxy_decrypt(txt_input, self.key.get())
        self.text_output.insert(tk.END, oxy_decrypt(txt_input, self.key.get()))
        self.historydict.update({txt_input: after})

    def press_clear(self):
        self.text_input.delete("1.0", tk.END)
        self.text_output.delete("1.0", tk.END)
        
    def press_copy(self):
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.text_output.get("1.0", "end-1c"))

    def press_history(self):
        f = open("oxy_history.txt", "w")
        f.write("{\n")
        for k in self.historydict.keys():
            f.write(f"'{k}':'{self.historydict[k]}'\n")
        f.write("}")
        f.close()
        webbrowser.open("oxy_history.txt")

    def toggle_password(self):
        if self.key_input.cget('show') == '':
            self.key_input.config(show='*')
            self.show_password.config(text='Show Password')
        else:
            self.key_input.config(show='')
            self.show_password.config(text='Hide Password')

if __name__ == "__main__":
    try:
        app = Oxydierer()
        app.run()
    finally:
        open('oxy_history.txt', 'w').close()