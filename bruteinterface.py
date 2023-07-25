import customtkinter as tk
from bruteforce import brute

result = None

root = tk.CTk()

root.geometry("400x600")
root.title("BruteForcer")
root.iconbitmap('download.ico')
user_label = tk.CTkLabel(root, text="BruteForce Risky Bank", font=("Arial", 20))
user_label.pack(pady=10)
username = tk.CTkEntry(root, placeholder_text="Target UserName")
username.pack(pady=2, ipadx=40)
button = tk.CTkButton(root, text="Start Brute", command=lambda: brute(username.get(), text_field))
button.pack(pady=5)
text_field = tk.CTkTextbox(root, fg_color="#eee", corner_radius=0, text_color='black')

text_field.place(rely=0.3, relwidth=1, relheight=0.6)
root.mainloop()