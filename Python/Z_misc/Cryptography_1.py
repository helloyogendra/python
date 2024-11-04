# pip install cryptography
# AES encryption (symmetric-key algorithm).

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generate key and IV
key = os.urandom(32)            # AES-256 key
iv = os.urandom(16)             # Initialization Vector (IV)

print(f'key = {key}, iv = {iv}')

# Encrypt
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(b"My Secret Message") + encryptor.finalize()

# Decrypt
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print("Plaintext:", plaintext.decode())
