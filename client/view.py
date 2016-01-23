#!/usr/bin/env python
# -*- coding: utf-8 -*-
from steganography import *
from settings import HOST, PORT_S, ROOT, USER, PORT_R
from tkinter import *
import socket
__author__ = 'piotrowy'


class Chat(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.set_meta_view(master)
        self.create_widgets()

    @staticmethod
    def set_meta_view(master) -> object:
        master.title("Client")
        master.geometry('410x390')
        master.resizable(width=FALSE, height=FALSE)

    def create_widgets(self):
        self.chat_log = Text(self, bd=0, bg='white', height=17, width='43', font='Arial', state=DISABLED)
        self.scrollbar = Scrollbar(self, command=self.chat_log.yview)
        self.chat_entry = Text(self, bd=0, bg='white', height=3, width='33', font='Arial')
        self.button_send = Button(self, text="Send", width=7, command=self.send_to_server)
        self.button_quit = Button(self, text="Set", width=7, fg="red", command=self.set_server)

        self.chat_log.grid(row=0, column=0)
        self.scrollbar.grid(row=0, column=1, sticky=(N, E))
        self.chat_entry.grid(row=1, column=0, sticky=(N, W))
        self.button_send.grid(row=1, column=0, sticky=(N, E))
        self.button_quit.grid(row=1, column=0, sticky=(S, E))

        self.chat_entry.bind("<Return>", self.send_to_server)
        self.chat_entry.bind("<KeyRelease-Return>", self.clear_entry)

    def show_statement(self, txt):
        self.load_message(txt, ROOT)
        self.clear_entry()

    def load_message(self, message, user, convert=None):
        self.chat_log.config(state=NORMAL)
        start = float(self.chat_log.index('end'))-1.0
        self.chat_log.insert(END, user + ': ')
        self.chat_log.insert(END, self.msg_filter(message))
        self.chat_log.tag_add(user + ': ', start, start+float((len(user)+1)/10))
        if user == USER:
            self.chat_log.tag_config(user + ': ', foreground='#445599')
        elif user == ROOT:
            self.chat_log.tag_config(user + ': ', foreground='#FF4455')
        else:
            self.chat_log.tag_config(user + ': ', foreground='#449955')
        self.chat_log.config(state=DISABLED)
        self.chat_log.yview(END)

    def clear_entry(self, event=None):
        self.chat_entry.delete("0.0", END)

    def send_to_server(self, event=None):
        message = self.msg_filter(self.chat_entry.get("0.0", END))
        if message != '' and message != '\n':
            print('[send_to_server] message: ' + message)
            sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sck.connect((HOST, PORT_S))
                print('[send_to_server]: Connection established.\n')
            except socket.error:
                print('[send_to_server]: Connection can\'t be established.\n')
                return
            sck.send(message.encode('utf-8'))
            sck.close()
        self.clear_entry()

    def set_server(self):
        server_data = self.chat_entry.get("0.0", END).split(' ')
        if len(server_data) == 4:
            USER = server_data[0]
            HOST = server_data[1]
            PORT_S = int(server_data[2])
            PORT_R = int(server_data[3])
            self.show_statement('User: ' + USER + ', Host: ' + HOST + ', Port_s: ' + str(PORT_S) + ', Port_r: ' + PORT_R)
        else:
            self.show_statement('Invalid data. \n')
            self.show_statement('User: ' + USER + ', Host: ' + HOST + ', Port_s: ' + str(PORT_S) + ', Port_r: ' + PORT_R)
        self.clear_entry(self)

    @staticmethod
    def msg_filter(txt):
        message = ''
        for i in range(len(txt)):
            if txt[i] != '\n' or txt[i] != ' ':
                message = txt[i:]
                break
        for i in range(1, len(message)):
            if message[len(message)-i] != '\n' or message[len(message)-i] != ' ':
                return message[:len(message)-i] + '\n'
        return ''

