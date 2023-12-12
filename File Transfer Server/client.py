import socket
import ssl
import file_transfer

def connect_to_server(server_address, username, password):
    try:
        sock = socket.create_connection((server_address, 5000))
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE  # Disable certificate verification
        secure_socket = context.wrap_socket(sock, server_hostname=server_address)

        secure_socket.sendall(username.encode())
        secure_socket.sendall(password.encode())

        response = secure_socket.recv(1024).decode()
        if response == "Success":
            return secure_socket
        else:
            secure_socket.close()
            return None
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def upload_file(secure_socket, file_path):
    try:
        with open(file_path, 'rb') as file:
            secure_socket.sendall(b'UPLOAD')
            while chunk := file.read(1024):
                secure_socket.sendall(chunk)
        print("File uploaded successfully.")
    except Exception as e:
        print(f"Upload error: {e}")

def download_file(secure_socket, file_path):
    try:
        secure_socket.sendall(b'DOWNLOAD')
        with open(file_path, 'wb') as file:
            while True:
                data = secure_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        print("File downloaded successfully.")
    except Exception as e:
        print(f"Download error: {e}")