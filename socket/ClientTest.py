# coding: utf-8
__author__ = 'hano'
import socket


BUF_SIZE = 1024


def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 4321))
    client_socket.send("hello server")
    while True:
        data = client_socket.recv(BUF_SIZE)
        if data:
            print 'server say ', client_socket.recv(BUF_SIZE), '\n'


def udp_client():
    ADDR = ('127.0.0.1', 4322)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto('hello udp server', ADDR)
    while True:
        data, ADDR = client_socket.recvfrom(BUF_SIZE)
        if data:
            print 'udp server ', ADDR, ' say ', data, '\n'


if __name__ == '__main__':
    udp_client()
