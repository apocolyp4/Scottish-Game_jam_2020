import socket
import threading

ENCODING = 'utf-8'

class Receiver(threading.Thread):

    def __init__(self, my_host, my_port, in_q):
        self.host = my_host
        self.port = my_port
        self.in_q = in_q
        threading.Thread.__init__(self, name="messenger_receiver", args=(self.in_q,))

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(10)
        while True:
            connection, client_address = sock.accept()
            try:
                full_message = ""
                while True:
                    data = connection.recv(16)
                    full_message = full_message + data.decode(ENCODING)
                    if not data:
                        self.in_q.put(full_message.strip())
                        break
            finally:
                connection.shutdown(2)
                connection.close()

    def run(self):
        self.listen()


class Sender(threading.Thread):

    def __init__(self, my_friends_host, my_friends_port, out_q):
        self.host = my_friends_host
        self.port = my_friends_port
        self.out_q = out_q
        threading.Thread.__init__(self, name="messenger_sender", args=(self.out_q,))


    def run(self):
        while True:
            message = self.out_q.get()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            s.sendall(message.encode(ENCODING))
            s.shutdown(2)
            s.close()
