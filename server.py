import socket
import sqlite3
import pickle

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8080
soc.bind((host, port))
soc.listen()
print("***** server starting *****")
try:
    conn, addr = soc.accept()
    print("**** server now active ****")
except Exception as e:
    print(e)


db_conn = sqlite3.connect("Accounts.db")
c = db_conn.cursor()

while True:
    credential = conn.recv(2024)
    if credential == b'':
        conn, addr = soc.accept()
        print("**** server now reactivating ****")
    else:
        credential = pickle.loads(credential)
        print(credential)
        c.execute("SELECT * FROM USERS WHERE NAME=? AND PASSWD=?", [credential[0], credential[1]])
        result = c.fetchone()
        if result is None:
            conn.send(pickle.dumps("False"))
            print(f"Request from {conn}")
        else:
            print(result)
            conn.send(pickle.dumps(result))
            print(result)
