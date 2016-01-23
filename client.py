#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import view

__author__ = 'piotrowy'

root = tk.Tk()
app = view.Chat(master=root)


def main():
    app.mainloop()

if __name__ == '__main__':
    main()
