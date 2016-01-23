from client import *
from socket import *
__author__ = 'piotrowy'

HOST = '127.0.0.1'
PORT = 8011
sck = socket(AF_INET, SOCK_STREAM)


def receive_from_server(root):
    try:
        sck.connect(HOST, PORT)
        app.load_message(message='Connection established', user='root')
    except error:
        app.load_message(message='Connection can\'t be established', user='root')
        return
