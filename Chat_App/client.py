import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def send_message():
    message = entry.get()
    if message:
        client_socket.send(message.encode('utf-8'))
        entry.delete(0, tk.END)

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            text_area.insert(tk.END, f'{message}\n')
            text_area.yview(tk.END)
        except Exception as e:
            print(e)
            break

def connect_to_server():
    global client_socket
    username = username_entry.get()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5555))
    client_socket.send(username.encode('utf-8'))
    threading.Thread(target=receive_message).start()
    login_frame.destroy()

root = tk.Tk()
root.title('Chat Application')

login_frame = tk.Frame(root)
login_frame.pack(pady=10)

tk.Label(login_frame, text='Enter your username:').pack()
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=10)

tk.Button(login_frame, text='Connect', command=connect_to_server).pack()

message_frame = tk.Frame(root)
text_area = scrolledtext.ScrolledText(message_frame, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=10)
entry = tk.Entry(message_frame, width=30)
entry.pack(padx=10, pady=10)
send_button = tk.Button(message_frame, text='Send', command=send_message)
send_button.pack(pady=10)

message_frame.pack(pady=10)

root.mainloop()
