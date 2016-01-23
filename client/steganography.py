#!/usr/bin/env python
# -*- coding: utf-8 -*-
import skimage as skm
__author__ = 'piotrowy'

lena_image = [[]]


def encode_secret_message(msg):
    pass


def decode_secret_message(msg):
    pass


def encode_to_sockets(str_table):
    pass


def decode_from_sockets(socket_string):
    data = [[]]
    index = 0
    for i in range(len(lena_image)):
        for j in range(len(lena_image[i])):
            data[i][j] = int(socket_string[index])
            index += 1
    return data
