import tkinter as tk
from tkinter import filedialog, messagebox
import client  

class FileTransferClientUI:
    def __init__(self, root):
        self.root = root
        root.title('File Transfer Client')

        tk.Label(root, text='Server Address:').grid(row=0, column=0)
        self.server_address_entry = tk.Entry(root)
        self.server_address_entry.grid(row=0, column=1)

        tk.Label(root, text='Username:').grid(row=1, column=0)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=1, column=1)

        tk.Label(root, text='Password:').grid(row=2, column=0)
        self.password_entry = tk.Entry(root, show='*')
        self.password_entry.grid(row=2, column=1)

        self.connect_button = tk.Button(root, text='Connect', command=self.connect_to_server)
        self.connect_button.grid(row=3, columnspan=2)

        self.upload_button = tk.Button(root, text='Upload File', command=self.upload_file, state=tk.DISABLED)
        self.upload_button.grid(row=4, columnspan=2)

        self.download_button = tk.Button(root, text='Download File', command=self.download_file, state=tk.DISABLED)
        self.download_button.grid(row=5, columnspan=2)

    def connect_to_server(self):
        server_address = self.server_address_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        if client.connect_to_server(server_address, username, password):
            messagebox.showinfo("Info", "Connected to Server")
            self.upload_button['state'] = tk.NORMAL
            self.download_button['state'] = tk.NORMAL
        else:
            messagebox.showerror("Error", "Failed to connect to Server")

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Here add logic to upload the file
            # For example: client.upload_file(file_path)
            messagebox.showinfo("Info", "File uploaded successfully")

    def download_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            secure_socket = self.connect_to_server()
            if secure_socket:
                client.download_file(secure_socket, file_path)
                messagebox.showinfo("Info", "File downloaded successfully")
            else:
                messagebox.showerror("Error", "Failed to download file")

if __name__ == '__main__':
    root = tk.Tk()
    app = FileTransferClientUI(root)
    root.mainloop()