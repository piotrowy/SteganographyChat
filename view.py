import tkinter as tk
__author__ = 'piotrowy'


class Chat(tk.Frame):
    button_send = None,
    button_server = None,
    button_quit = None

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.set_meta_view(master)
        self.create_widgets(master)

    @staticmethod
    def set_meta_view(master) -> object:
        master.title("Client")
        master.minsize(400, 300)
        master.maxsize(1000, 1000)

    def create_widgets(self, root):
        self.button_send = tk.Button(self)
        self.button_send["text"] = "Hello World\n(click me)"
        self.button_send["command"] = self.say_hi
        self.button_send.pack(side="top")
        self.button_quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.button_quit.pack(side="bottom")

    @classmethod
    def say_hi(cls):
        print("hi there, everyone!")
