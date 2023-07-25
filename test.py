import customtkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from client import request


tk.set_appearance_mode('light')
tk.set_default_color_theme('green')
root = tk.CTk()
root.geometry("1200x600")
root.title("Risky BANK")
root.iconbitmap('download (1).ico')
root.minsize(1200, 600)


def swap():
    response = request(username.get(), password.get())
    if response != "False":
        trans_side_frame.tkraise()
        trans_main_frame.tkraise()
        main_label.configure(text=f"Wellcome {response[0]} \nChoose any options")
        accno_label.configure(text=f"Account Number: {response[3]}")
        name_label.configure(text=f"Account Name: {response[0]}")
        user_balance_label.configure(text=f"Available Balance: {response[2]} $")
        acc_password.configure(text=f"Password: {response[1]}")
    else:
        messagebox.showerror("invalid", "Wrong Credentials")

def change(frame):
    if frame == main_frame:
        side_frame.tkraise()
    frame.tkraise()


#----------------image----------------section
orginal_image = Image.open('risky.jpg').resize((600, 800))
modified_image = ImageTk.PhotoImage(orginal_image)

#--------------side frame---------------
side_frame = tk.CTkFrame(root, fg_color='#eafaee', corner_radius=0)
side_frame.place(x=0, y=0 ,relwidth=0.4, relheight=1)
img_label = tk.CTkLabel(side_frame,text="", image=modified_image)
img_label.pack()

#---------------main frame-------------
main_frame = tk.CTkFrame(root, corner_radius=0)
main_frame.place(relx=0.4, relwidth=0.6, relheight=1)
#-------------form section-------------
form_frame = tk.CTkFrame(main_frame, fg_color='#3e3e3e')
form_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.4, relheight=0.6)
label = tk.CTkLabel(form_frame, text="LogIn", text_color='#0f4', font=("Arial", 30))
label.place(relx=0.5, rely=0.18, anchor='center')
username = tk.CTkEntry(form_frame, placeholder_text="User Name")
username.place(relx=0.5, rely=0.34, anchor='center', relwidth=0.7)

password = tk.CTkEntry(form_frame, placeholder_text="Password", show="*")
password.place(relx=0.5, rely=0.45, anchor='center', relwidth=0.7)

button = tk.CTkButton(form_frame, text='SignIn', command=swap)
button.place(relx=0.5, rely=0.6, anchor='center', relwidth=0.4)



#-----------------after login trans-main frames----------------------
trans_main_frame = tk.CTkFrame(root, fg_color='#3e3e3e', corner_radius=0)
trans_main_frame.place(relx=0.4, relwidth=0.6, relheight=1)
main_label = tk.CTkLabel(trans_main_frame, text_color='#fff', font=("Arial", 35))
main_label.place(relx=0.5, rely=0.5, anchor='center')

#------------------after login trans-side -------------------------
trans_side_frame = tk.CTkFrame(root, fg_color='#eafaee', corner_radius=0)
trans_side_frame.place(x=0, y=0, relwidth=0.4, relheight=1)
side_label = tk.CTkLabel(trans_side_frame, text="")
side_label.pack(padx=30)
side_button1 = tk.CTkButton(trans_side_frame, text="Account Info", command=lambda :change(info_frame))
side_button1.pack(pady=10, ipadx=60, ipady=20)
side_button2 = tk.CTkButton(trans_side_frame, text="Transfer", command=lambda :change(transfer_frame))
side_button2.pack(pady=10, ipadx=60, ipady=20)
side_button3 = tk.CTkButton(trans_side_frame, text="Show Transactions")
side_button3.pack(pady=10, ipadx=60, ipady=20)
side_button4 = tk.CTkButton(trans_side_frame, text="Utility payment")
side_button4.pack(pady=10, ipadx=60, ipady=20)
side_button5 = tk.CTkButton(trans_side_frame, text="LogOut", command=lambda :change(main_frame))
side_button5.pack(pady=10, ipadx=60, ipady=20)

#--------------balance frame--------------------
info_frame = tk.CTkFrame(root, corner_radius=0)
info_frame.place(relx=0.4, relwidth=0.6, relheight=1)
cont = tk.CTkFrame(info_frame, fg_color="#3e3e3e")
cont.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.5, anchor='center')
name_label = tk.CTkLabel(cont,text="Account Name", text_color='#fff', font=("Arial",20))
name_label.place(relx=0.25, rely=0.2, )
accno_label = tk.CTkLabel(cont,text="Account Number", text_color='#fff', font=("Arial",20))
accno_label.place(relx=0.25, rely=0.3, )
user_balance_label = tk.CTkLabel(cont,text="Available balance: ", text_color='#fff', font=("Arial",20))
user_balance_label.place(relx=0.25, rely=0.4, )
acc_password = tk.CTkLabel(cont, text="Password: ", text_color='#fff', font=("Arial",20))
acc_password.place(relx=0.25, rely=0.5, )

#---------------transfer frame-------------------
transfer_frame = tk.CTkFrame(root, corner_radius=0)
transfer_frame.place(relx=0.4, relwidth=0.6, relheight=1)
cont2 = tk.CTkFrame(transfer_frame, fg_color="#3e3e3e")
cont2.place(relx=0.5, rely=0.5, relwidth=0.6, relheight=0.5, anchor='center')
transfer_label = tk.CTkLabel(cont2, text="Transfer To:", text_color='#fff')
transfer_label.place(relx=0.4, rely=0.3, anchor='center')
transfer_entry = tk.CTkEntry(cont2,placeholder_text="username", text_color='#000')
transfer_entry.place(relx=0.4, rely=0.4, anchor='center')
transfer_account_label = tk.CTkLabel(cont2, text="Account Number:", text_color='#fff')
transfer_account_label.place(relx=0.4, rely=0.5, anchor='center')
transfer_entry = tk.CTkEntry(cont2, text_color='#000', placeholder_text="10----")
transfer_entry.place(relx=0.4, rely=0.6, anchor='center')

main_frame.tkraise()
side_frame.tkraise()
root.mainloop()