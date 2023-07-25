import tkinter as tk
from tkinter import ttk
import pillow
root = tk.Tk()
root.geometry("1200x600")
root.title("RiskIT")
root.iconbitmap('download (1).ico')
root.minsize(600, 600)

def get():
    user = username.get()
    password = passwd.get()
    print(user, password)

menu_frame = ttk.Frame(root)
menu_frame.place(x=0, y=0, relwidth=0.4, relheight=1)
ttk.Label(menu_frame, background='#2323ff').pack(expand=True, fill='both')

main_frame = ttk.Frame(root)
main_frame.place(relx=0.4, relwidth=0.7, relheight=1)
form_frame = ttk.Frame(main_frame)
user_label = ttk.Label(form_frame, text="UserName")
username = ttk.Entry(form_frame)
passwd_label = ttk.Label(form_frame, text="Password")
passwd = ttk.Entry(form_frame)
main_frame.rowconfigure((0,1,2,3,4), weight=0)
main_frame.columnconfigure((0), weight=1)
user_label.grid(row=0, columnspan=3)
username.grid(row=1, ipadx=60)
passwd_label.grid(row=2)
passwd.grid(row=3, ipadx=60)
button = ttk.Button(form_frame, text="LogIn", command=get)
button.grid(row=4, column=0)
form_frame.place(relx=0.4, rely=0.4, anchor='center')
root.mainloop()
