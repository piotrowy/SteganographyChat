#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from skimage import data
from skimage.color import rgb2gray
__author__ = 'piotrowy'


def encode_secret_message(img):
    out_string = ''
    for i in range(len(img)):
        for j in range(len(img[i])):
            out_string += chr(int(img[i][j]))
    return out_string


def decode_secret_message(image):
    pass


def encode_to_sockets(message, user):
    message = user + '#' + str(time.clock()) + '#' + message
    data_to_encode = []
    index = 0
    image = rgb2gray(data.lena())
    for i in range(len(message)):
        #biore jeden znak z message. Dalej biore jego numer ASCII? i do bin
        bin_msg = bin(int(message[i].encode()[0])) #tutaj sie gowno pieprzy bo binarne zapisy maja rozna dlugosc
        for n, value in enumerate(reversed(bin_msg)):
            if value == 'b':
                break
            data_to_encode.append(int(value))
        if len(bin_msg)-2 < 8:#teraz chyba powinna sie zgadzac kazdy string jest zapisany na 8 znakach???
            for number_of_zeros_to_add in range(0, 8-len(bin_msg-2)):
                data_to_encode.append(int(0))
    for i in range(len(image)):
        for j in range(len(image[i])):
            if index < len(data_to_encode):
                image[i][j] = int(image[i][j]*255.0) + data_to_encode[index]
                index += 1
            else:
                image[i][j] = int((image[i][j]*255.0) % 255)
    return image


def decode_from_sockets(socket_string):
    image = rgb2gray(data.lena())
    data_str = []
    index = 0
    socket_string = socket_string[:len(socket_string)-1]
    for i in range(len(image)):
        data_str.append([])
        for j in range(len(image[i])):
            if index < len(socket_string) - 1:
                data_str[i].append(ord(socket_string[index]))
                index += 1
            else:
                break
    return data_str
