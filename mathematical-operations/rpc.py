import socket

from server_helpers import send_data, receive_data
from server_operations import Operation


class MathematicalOperations:

    def __init__(self, server_address, server_port):
        self.__server_address = server_address
        self.__server_port = server_port

    def sum(self, a, b):
        args = [Operation.sum, a, b]
        return self.request_operation(args)

    def product(self, a, b):
        args = [Operation.product, a, b]
        return self.request_operation(args)

    def factorial(self, value):
        args = [Operation.factorial, value]
        return self.request_operation(args)

    def create_connection(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.__server_address, self.__server_port))
        return sock

    def request_operation(self, args):
        sock = self.create_connection()
        send_data(args, sock)

        result = receive_data(sock)
        sock.close()
        return result
