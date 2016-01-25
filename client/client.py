#!/usr/bin/env python
# -*- coding: utf-8 -*-
from view import Chat
from settings import HOST, PORT_R, USER
import steganography as steg
import tkinter as tk
import socket
import _thread
import time
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
        while data.decode("ISO-8859-1") != '':
            data_str += data.decode("ISO-8859-1")
            data = sck.recv(256)
        sck.close()

        if already_used == 0:
            already_used += 1
            data_table = data_str.split('\n')
            for i in range(len(data_table)):
                if data_table[i] != '' and data_table[i] != '\n':
                    app.load_message(steg.decode_secret_message(steg.decode_from_sockets(data_table[i])))
        else:
            data_temp_table = data_str.split('\n')
            for i in range(len(data_table)):
                for j in range(len(data_temp_table)):
                    if data_table[i] != data_temp_table[j] and data_temp_table[j] != '' and data_temp_table[j] != '\n':
                        app.load_message(steg.decode_secret_message(steg.decode_from_sockets(data_temp_table[i])))
            data_table = data_temp_table
        time.sleep(0.5)


def main():
    _thread.start_new_thread(receive_from_server, ())
    app.mainloop()


if __name__ == '__main__':
    main()
