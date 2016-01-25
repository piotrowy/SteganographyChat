#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from skimage import data
from skimage.color import rgb2gray
__author__ = 'piotrowy'

lena_image = [[]]


def encode_secret_message(img):
    out_string = ''
    for i in range(len(img)):
        for j in range(len(img[i])):
            out_string += chr(int(img[i][j]))
    return out_string + '\n'


def decode_secret_message(image):
    binary_char = ''
    index = 0
    message = ''
    for i in range(len(image)):
        for j in range(len(image[i])):
            if index == 8:
                index = 0
                message += chr(int(binary_char, 2))
                binary_char = ''
            if image[i][j] % 2 == 0:
                binary_char += '0'
            else:
                binary_char += '1'
            index += 1
    message = message.split('#@$@#')
    return message[0], message[1], message[2]


def encode_char_to_binary(char):
    bin_char = bin(ord(char))
    bin_char = bin_char[2:]
    for i in range(8-len(bin_char)):
        bin_char = '0' + bin_char
    return bin_char


def write_to_pixel(arg, pix):
    to_map = str(int(arg) % 2) + str(int(pix) % 2)
    return {'00': int(pix),
            '01': int(pix) + 1,
            '10': int(pix) + 1,
            '11': int(pix)}[to_map]


def encode_to_sockets(message, user):
    message = user + '#@$@#' + str(time.clock()) + '#@$@#' + message + '#@$@#'
    index = 0
    image = rgb2gray(data.lena())
    binary_message = ''
    for i in range(len(message)):
        binary_message += encode_char_to_binary(message[i])
    for i in range(len(image)):
        for j in range(len(image[i])):
            if index < len(binary_message):
                image[i][j] = write_to_pixel(binary_message[index], image[i][j])
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
            if index < len(socket_string)-1:
                data_str[i].append(ord(socket_string[index]))
                index += 1
            else:
                data_str[i].append(image[i][j])
    return data_str


def main():
    print(decode_secret_message(decode_from_sockets(encode_secret_message(encode_to_sockets('Nie jestem tutaj.\n', 'Piotr')))))


if __name__ == '__main__':
    main()
