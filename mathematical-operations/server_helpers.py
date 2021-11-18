import pickle

HEADER_SIZE = 10


def send_data(data, client_socket, header_size=HEADER_SIZE):
    msg = pickle.dumps(data)
    msg = bytes(f"{len(msg):<{header_size}}", 'utf-8') + msg
    client_socket.send(msg)


def receive_data(client_socket, header_size=HEADER_SIZE):
    while True:
        msg_len = 0
        full_msg = b''
        new_msg = True

        while True:
            msg = client_socket.recv(16)

            if new_msg:
                try:
                    msg_len = int(msg[:header_size])
                except RuntimeError:
                    msg_len = 0
                new_msg = False

            full_msg += msg

            if len(full_msg) - header_size == msg_len:
                return pickle.loads(full_msg[header_size:])
