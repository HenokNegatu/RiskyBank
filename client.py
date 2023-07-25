import pickle
import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8080
soc.connect((host, port))


def request(name, passwd):
    credential = [name, passwd]
    credental = pickle.dumps(credential)
    try:
        global data
        soc.send(credental)
        data = pickle.loads(soc.recv(4097))

        return data
    except Exception as e:
        print(e)
