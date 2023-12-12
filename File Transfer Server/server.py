import socket
import threading
import file_transfer
import auth
import logger
import ssl

def handle_client(client_socket):
    try:
        username = client_socket.recv(1024).decode()
        password = client_socket.recv(1024).decode()
        if username == "user" and auth.verify_password(password):
        # if auth.authenticate(username, password):
            logger.log_event(f"Authenticated user: {username}")
            while True:
                command = client_socket.recv(1024).decode()
                if command == 'UPLOAD':
                    # Add logic for handling file upload
                    pass
                elif command == 'DOWNLOAD':
                    # Add logic for handling file download
                    pass
        else:
            logger.log_event("Authentication failed")
            client_socket.close()
    except Exception as e:
        logger.log_event(f"Error: {e}")
    finally:
        client_socket.close()
        logger.log_event("Client disconnected")

def start_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # Update these lines to use the generated certificates
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    context.verify_mode = ssl.CERT_NONE

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost', 5000))
        server_socket.listen(5)
        logger.log_event("Server listening on port 5000")

        while True:
            client_socket, addr = server_socket.accept()
            secure_socket = context.wrap_socket(client_socket, server_side=True)
            logger.log_event(f"Connection from {addr} has been established.")
            client_thread = threading.Thread(target=handle_client, args=(secure_socket,))
            client_thread.start()

if __name__ == "__main__":
    start_server()