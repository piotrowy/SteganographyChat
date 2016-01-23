#!/usr/bin/env python
# -*- coding: utf-8 -*-
from view import Chat
from settings import HOST, PORT_R
import tkinter as tk
import socket
import _thread
__author__ = 'piotrowy'

root = tk.Tk()
app = Chat(master=root)


def receive_from_server():
    while True:
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sck.connect((HOST, PORT_R))
        except socket.error:
            print('[SOCKETS.PY][receive_from_server]: Connection can\'t be established')
        data = sck.recv(15)
        if data != '':
            app.load_message(data, '', convert=True)
        sck.close()


def main():
    _thread.start_new_thread(receive_from_server,())
    app.mainloop()


if __name__ == '__main__':
    main()
