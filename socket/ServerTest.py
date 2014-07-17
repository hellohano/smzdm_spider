# coding: utf-8
__author__ = 'hano'

import socket


BUF_SIZE = 1024


def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 4321))
    server_socket.listen(5)
    while True:
        client_socket, addr = server_socket.accept()
        print 'the client ', client_socket, ' is ', addr
        client_say = client_socket.recv(BUF_SIZE)
        if client_say is not None:
            print 'the client say', client_say
            client_socket.send("hello client")
            client_socket.send("hello client1")
            client_socket.send("hello client2")
            client_socket.close()
    server_socket.close()


def udp_server():
    address = ('127.0.0.1', 4322)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(address)
    print 'watiing for message ...'
    while True:
        data, addr = server_socket.recvfrom(BUF_SIZE)
        print 'receiver data from ', addr, 'the addr == ', addr
        server_socket.sendto('hello upd client', addr)
    server_socket.close()


if __name__ == '__main__':
    udp_server()


