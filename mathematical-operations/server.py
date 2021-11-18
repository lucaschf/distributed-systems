import multiprocessing
import socket

from server_helpers import send_data, receive_data
from server_operations import Operation
import logging

from math import factorial as fact

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("")


def product(a, b):
    return a * b


def factorial(value):
    return fact(value)


def sum_(a, b):
    return a + b


def answer(connection, data, requested_operation):
    send_data(data, connection)
    logger.info("Operation: '{}'; Answer: {}".format(requested_operation, str(data)))
    logger.info("Closing connection.")
    connection.close()


def handle(connection, address):
    try:
        logger.info(f"Connection from {address} has been established.")

        while True:
            data = receive_data(connection)
            logger.info(f"Received request {str(data)}")

            if data == "":
                logger.debug(f"No data received. Connection with {address} closed.")
                answer(connection, "Invalid request", str(data))
                break
            if Operation.product == data[0]:
                answer(connection, product(data[1], data[2]), f"Product of {data[1]},{data[2]}")
                break
            if Operation.factorial == data[0]:
                answer(connection, factorial(data[1]), f"Factorial of {str(data[1])}")
                break
            if Operation.sum == data[0]:
                answer(connection, sum_(data[1], data[2]), f"Sum {data[1]},{data[2]}")
                break
            else:
                logger.info("Unsupported operation")
                answer(connection, "Unsupported operation", str(data))
                break

    except RuntimeError:
        logger.exception("Can't handle request")
        answer(connection, "Can't handle request", "")


class Server(object):

    def __init__(self, hostname, port):
        self.logger = logging.getLogger("")
        self.hostname = hostname
        self.port = port
        self.socket = None

    def start(self):
        self.logger.info("Server ready...")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        while True:
            conn, address = self.socket.accept()
            self.logger.info("Connection accepted...")
            _process = multiprocessing.Process(target=handle, args=(conn, address))
            _process.daemon = True
            _process.start()
            self.logger.debug("Started process %r", _process)


if __name__ == "__main__":

    server_address = "10.0.1.15"
    server_port = 12000

    server = Server(server_address, server_port)

    try:
        server.start()
    except RuntimeError:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting down")
        for process in multiprocessing.active_children():
            logging.info("Shutting down process %r", process)
            process.terminate()
            process.join()

    logging.info("All done")
