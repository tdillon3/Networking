# Overview

As a software engineer seeking to deepen my understanding of networked applications, I embarked on a project to develop a file transfer system. This application demonstrates the fundamental concepts of network communication, specifically focusing on a client-server architecture.

The software comprises two main components: a server that listens for file transfer requests and a client with a graphical user interface (GUI) allowing users to upload and download files to and from the server.

To use the software:
1. **Start the Server**: Run `server.py`. It listens for incoming connections and handles file requests.
2. **Run the Client UI**: Execute `UI.py`. In the GUI, enter server details and credentials, then connect to the server. You can then upload and download files.

This project serves as a practical application of network communication concepts and helps in grasping the intricacies of building networked applications.

[Software Demo Video](https://www.loom.com/share/7abeecaf0a1444ccba290fa7cc630cea?sid=c537f9b2-f50c-419a-b25b-868e92a932e6)

# Network Communication

The application follows a **client-server architecture**:
- **Protocol**: Utilizes **TCP (Transmission Control Protocol)** for reliable data transmission.
- **Port**: Uses port `5000` for network communication.
- **Message Format**: Employs simple text-based commands such as 'UPLOAD' and 'DOWNLOAD', followed by the file data.

# Development Environment

Tools and technologies used in this project:
- **IDE**: Visual Studio Code
- **Language**: Python
- **Libraries**:
  - `socket` for networking
  - `ssl` for encrypted communication
  - `tkinter` for the GUI
  - `bcrypt` for secure password hashing
  - `cryptography` for generating SSL certificates

# Useful Websites

* [Python Official Documentation](https://docs.python.org/3/)
* [Stack Overflow](https://stackoverflow.com/)
* [GeeksforGeeks - Python](https://www.geeksforgeeks.org/python-programming-language/)

# Future Work

Future enhancements for the project include:
* **Robust Authentication System**: Upgrading from hardcoded checks to a dynamic authentication system.
* **Support for Various File Types**: Enhancing the app to handle multiple file formats.
* **Improved Security**: Implementing further security measures and encryption.

# Security Implementation

- **Bcrypt for Passwords**: The project uses `bcrypt` to hash passwords, providing a secure way to store and verify user credentials.
- **SSL Certificate Generation**: `generate_cert.py` utilizes the `cryptography` library to create SSL certificates. This script simplifies the process of generating self-signed certificates for secure communication between the client and server.