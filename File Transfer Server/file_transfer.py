import os
import socket

def send_file(client_socket: socket.socket, file_path: str):
    with open(file_path, 'rb') as file:
        while chunk := file.read(1024):
            client_socket.sendall(chunk)

def receive_file(client_socket: socket.socket, save_path: str):
    with open(save_path, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

def list_files(directory: str):
    return os.listdir(directory)

def delete_file(file_path: str):
    os.remove(file_path)

def rename_file(original_path: str, new_name: str):
    os.rename(original_path, new_name)