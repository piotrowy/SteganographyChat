#!/usr/bin/env python
# -*- coding: utf-8 -*-
import skimage as skm
import time
__author__ = 'piotrowy'

lena_image = [[]]


def encode_secret_message(img):
    out_string = ''
    for i in range(len(lena_image)):
        for j in range(len(lena_image[i])):
            out_string += str(img[i][j])
    return out_string + '\n'


def decode_secret_message(msg):
    pass


def encode_to_sockets(message, user):
    message = user + '#' + str(time.clock()) + '#' +  message
    data_to_encode = []
    index = 0
    image = [[]] #tu trzeba wstawic lenke z biblioteki ofc as_grey
    for i in range(len(message)):
        #biore jeden znak z message. Dalej biore jego numer ASCII? i do bin
        bin_msg = bin(int(message[i].encode()[0]))
        for n, value in enumerate(reversed(bin_msg)):
            if value == 'b':
                break
            data_to_encode.append(int(value))
    for i in range(len(lena_image)):
        for j in range(len(lena_image[i])):
            if index < len(data_to_encode):
                image[i][j] += data_to_encode[index]
                index += 1
            break
    return image


def decode_from_sockets(socket_string):
    data = [[]]
    index = 0
    socket_string = socket_string[:len(socket_string)-1]
    for i in range(len(lena_image)):
        for j in range(len(lena_image[i])):
            data[i][j] = int(socket_string[index])
            index += 1
    return data
