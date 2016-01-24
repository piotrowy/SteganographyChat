#!/usr/bin/env python
# -*- coding: utf-8 -*-
import settings as stg
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
        master.geometry('411x391')
        master.resizable(width=FALSE, height=FALSE)

    def create_widgets(self):
        self.chat_log = Text(self, bd=0, bg='white', height=18, width='49', font=("Arial", 11), state=DISABLED)
        self.scrollbar = Scrollbar(self, command=self.chat_log.yview)
        self.chat_entry = Text(self, bd=0, bg='white', height=3, width='34', font=("Arial", 12))
        self.button_send = Button(self, text="Send", width=7, command=self.send_to_server)
        self.button_quit = Button(self, text="Set", width=7, fg="red", command=self.set_server)

        self.chat_log.grid(row=0, column=0)
        self.scrollbar.grid(row=0, column=1, sticky=(N, E))
        self.chat_entry.grid(row=1, column=0, sticky=(N, W))
        self.button_send.grid(row=1, column=0, sticky=(N, E))
        self.button_quit.grid(row=1, column=0, sticky=(S, E))

        self.chat_entry.bind("<Return>", self.send_to_server)
        self.chat_entry.bind("<KeyRelease-Return>", self.clear_entry)

        self.show_statement('Type to set options [User] [Host] [Port_to_send] [Port_to_receive] and press \'set\'.\n')

    def show_statement(self, txt):
        self.load_message(txt, stg.ROOT)
        self.clear_entry()

    def load_message(self, message, user):
        if message != '' and message != '\n':
            self.chat_log.config(state=NORMAL)
            start = float(self.chat_log.index('end'))-1.0
            self.chat_log.insert(END, user + ': ')
            self.chat_log.insert(END, self.msg_filter(message))
            self.chat_log.tag_add(user + ': ', start, start+float((len(user)+1)/10))
            if user == stg.USER:
                self.chat_log.tag_config(user + ': ', foreground='#445599')
            elif user == stg.ROOT:
                self.chat_log.tag_config(user + ': ', foreground='#FF4455')
            else:
                self.chat_log.tag_config(user + ': ', foreground='#449955')
            self.chat_log.config(state=DISABLED)
            self.chat_log.yview(END)

    def clear_entry(self, event=None):
        self.chat_entry.delete("0.0", END)

    def clear_chat_log(self):
        self.chat_log.config(state=NORMAL)
        self.chat_log.delete("0.0", END)
        self.chat_log.config(state=DISABLED)
        return 0

    def check_command(self, message):
        print('[check_command]: ' + message)
        try:
            return {'/clear': self.clear_chat_log}[message]()
        except KeyError:
            return 1

    def send_to_server(self, event=None):
        message = self.msg_filter(self.chat_entry.get("0.0", END))
        self.clear_entry()
        if self.check_command(message[:len(message)-1]) != 0:
            if message != '' and message != '\n':
                print('[send_to_server] message: ' + message)
                sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    sck.connect((stg.HOST, stg.PORT_S))
                    print('[send_to_server]: Connection established.\n')
                except socket.error:
                    print('[send_to_server]: Connection can\'t be established.\n')
                    self.clear_entry()
                    return
                sck.send(message.encode('utf-8'))
                sck.close()

    def set_server(self):
        server_data = self.chat_entry.get("0.0", END).split(' ')
        if len(server_data) == 4:
            stg.USER = server_data[0]
            stg.HOST = server_data[1]
            stg.PORT_S = int(server_data[2])
            stg.PORT_R = int(server_data[3])
            self.show_statement('User: ' + stg.USER + ', Host: ' + stg.HOST + ', Port_s: ' + str(stg.PORT_S) + ', Port_r: ' + str(stg.PORT_R) + '\n')
        else:
            self.show_statement('Invalid data. \n')
            self.show_statement('Type to set options: [User] [Host] [Port_to_send] [Port_to_receive]\n')
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
                return message[:len(message) - i + 1]
        return ''

