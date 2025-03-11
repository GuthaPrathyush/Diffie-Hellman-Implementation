import socket
import Diffie_Hellman
from Crypto.Cipher import DES
import hashlib

def pad(text):
    while len(text) % 8 != 0:
        text += " "
    return text

server_private = Diffie_Hellman.generate_private_key()
server_public = Diffie_Hellman.compute_public_key(server_private)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))
server.listen(1)

print("Server waiting for connection...")
conn, addr = server.accept()
print(f"Connected to {addr}")

conn.send(str(server_public).encode())

client_public = int(conn.recv(1024).decode())

shared_key = Diffie_Hellman.compute_shared_secret(client_public, server_private)
print(f"Server Shared Key: {shared_key}")

des_key = hashlib.md5(str(shared_key).encode()).digest()[:8]

cipher = DES.new(des_key, DES.MODE_ECB)
message = "Hello Client"
padded_msg = pad(message)
encrypted_msg = cipher.encrypt(padded_msg.encode())

conn.send(encrypted_msg)

conn.close()
server.close()
