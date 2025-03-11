import socket
import Diffie_Hellman
from Crypto.Cipher import DES
import hashlib

client_private = Diffie_Hellman.generate_private_key()
client_public = Diffie_Hellman.compute_public_key(client_private)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))

server_public = int(client.recv(1024).decode())

client.send(str(client_public).encode())

shared_key = Diffie_Hellman.compute_shared_secret(server_public, client_private)
print(f"Client Shared Key: {shared_key}")

des_key = hashlib.md5(str(shared_key).encode()).digest()[:8]

encrypted_msg = client.recv(1024)

cipher = DES.new(des_key, DES.MODE_ECB)
decrypted_msg = cipher.decrypt(encrypted_msg).decode().strip()

print(f"Decrypted Message: {decrypted_msg}")

client.close()
