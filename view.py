import tkinter as tk
from tkinter import *
__author__ = 'piotrowy'


class Chat(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.set_meta_view(master)
        self.create_widgets()

    @staticmethod
    def set_meta_view(master) -> object:
        master.title("Client")
        master.geometry('410x390')
        master.resizable(width=FALSE, height=FALSE)

    def create_widgets(self):
        self.chat_log = Text(self, bd=0, bg='white', height=17, width='45', font='Arial', state=DISABLED)
        self.chat_log.insert(END, 'nlkkj\ndfg\ndfg\ndfg\n')
        self.chat_entry = Text(self, bd=0, bg='white', height=3, width='35', font='Arial')
        self.button_send = Button(self, text="Send", width=7, command=self.send_message)
        self.button_quit = Button(self, text="Connect", width=7, fg="red", command=self.connect_server)

        self.chat_log.grid(row=0, column=0)
        self.chat_entry.grid(row=1, column=0, sticky=(N, W))
        self.button_send.grid(row=1, column=0, sticky=(N,E))
        self.button_quit.grid(row=1, column=0, sticky=(S,E))

    def send_message(self):
        print("YOU: " + self.chat_entry.get("0.0", END))
        self.chat_log.config(state=NORMAL)
        self.chat_log.insert(END, "YOU: " + self.chat_entry.get("0.0", END))
        self.chat_log.config(state=DISABLED)

    def load_message(self, msg):
        self.chat_log.config(state=NORMAL)
        self.chat_log.insert(END, "YOU: " + msg)
        self.chat_log.config(state=DISABLED)

    def connect_server(self):
        pass
