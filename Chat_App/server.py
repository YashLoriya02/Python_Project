import socket
import threading
import sqlite3

# SQLite database setup
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (username varchar(40), address varchar(50))')
conn.commit()

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

# List to store connected clients
clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'exit':
                remove_client(client)
            else:
                broadcast(message)
        except:
            remove_client(client)
            break

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            continue

def remove_client(client):
    if client in clients:
        clients.remove(client)
        username = client.recv(1024).decode('utf-8')
        cursor.execute('DELETE FROM users WHERE username=?', (username,))
        conn.commit()
        client.close()

def start_server():
    print("Server is listening for connections...")
    print("Ready to Connect.")
    while True:
        client, address = server.accept()
        username = client.recv(1024).decode('utf-8')
        clients.append(client)

        cursor.execute('INSERT INTO users VALUES (?, ?)', (username, str(address)))
        conn.commit()

        print(f"Connection established with {username} at {address}")
        broadcast(f'{username} has joined the chat.')

        # Start a new thread for each connected client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()
