#!/usr/bin/env python
# -*- coding: utf-8 -*-
from view import Chat
from settings import HOST, PORT_R, USER
import tkinter as tk
import socket
import _thread
from steganography import *
import skimage
__author__ = 'piotrowy'

root = tk.Tk()
app = Chat(master=root)


def receive_from_server():
    already_used = 0
    data_table = []
    while True:
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sck.connect((HOST, PORT_R))
        except socket.error:
            print('[SOCKETS.PY][receive_from_server]: Connection can\'t be established')
        data_str = ''
        data = sck.recv(256)
        while data.decode('utf-8') != '':
            data_str += data.decode('utf-8')
            data = sck.recv(256)
        sck.close()

        if already_used == 0:
            already_used += 1
            data_table = data_str.split('\n')
            for i in range(len(data_table)):
                app.load_message(data_table[i], USER)
        else:
            data_temp_table = data_str.split('\n')
            for i in range(len(data_table)):
                if data_table[i] != data_temp_table[i]:
                    app.load_message(data_temp_table[i] + '\n', USER)
            data_table = data_temp_table


def main():
    _thread.start_new_thread(receive_from_server, ())
    app.mainloop()


if __name__ == '__main__':
    main()
