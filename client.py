#!/usr/bin/env python
# -*- coding: utf-8 -*-
from view import Chat
import tkinter as tk
__author__ = 'piotrowy'

root = tk.Tk()
app = Chat(master=root)


def main():
    root.mainloop()


if __name__ == '__main__':
    main()
