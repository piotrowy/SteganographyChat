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
    return out_string


def decode_secret_message(image):
    binary_char = ''
    index = 0
    message = ''
    for i in range(len(image)):
        for j in range(len(image[i])):
            if index == 8:
                index = 0
                message += chr(int(binary_char[::-1], 2))
                binary_char = ''
            if image[i][j] % 2 == 0:
                binary_char += '0'
            else:
                binary_char += '1'
            index += 1
    message = message.split('#@$@#')
    print(message)
    return message[0], message[1], message[2] + '\n'


def encode_to_sockets(message, user):
    message = user + '#@$@#' + str(time.clock()) + '#@$@#' + message + '#@$@#'
    data_to_encode = []
    index = 0
    image = rgb2gray(data.lena())
    for i in range(len(message)):
        #biore jeden znak z message. Dalej biore jego numer ASCII? i do bin
        bin_msg = bin(int(message[i].encode()[0]))#chr(int(bin(int('abc'.encode()[1])),2))
        #tutaj sie gowno pieprzy bo binarne zapisy maja rozna dlugosc
        for n, value in enumerate(reversed(bin_msg)):
            if len(bin_msg)-2 <= 8 and value == 'b':#teraz chyba powinna sie zgadzac kazdy string jest zapisany na 8 znakach???
                for number_of_zeros_to_add in range(0, 8-(len(bin_msg)-2)):
                    data_to_encode.append(0)
                    break
            if value == 'b':
                break
            data_to_encode.append(int(value))
    for i in range(len(image)):
        for j in range(len(image[i])):
            if index < len(data_to_encode):
                if data_to_encode[index] % 2 == 0:
                    if int(image[i][j]*255.0) % 2 == 1:
                        image[i][j] = int(image[i][j]*255.0) + 1
                    else:
                        image[i][j] = int(image[i][j]*255.0)
                else:
                    if int(image[i][j]*255.0) % 2 == 0:
                        image[i][j] = int(image[i][j]*255.0) + 1
                    else:
                        image[i][j] = int(image[i][j]*255.0)
                index += 1
            else:
                image[i][j] = int((image[i][j]*255.0) % 255)
    print(image[0])
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


def main():
    print(decode_secret_message(decode_from_sockets(encode_secret_message(encode_to_sockets('Jestem tutaj.\n', 'Piotr')) + '\n')))


if __name__ == '__main__':
    main()
