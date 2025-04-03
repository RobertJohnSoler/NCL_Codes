from Crypto.Cipher import AES

timestamp_bytes = b"1672531200"
key = timestamp_bytes.ljust(16, b'\0')  # exactly 16 bytes
iv = b'\x00' * 16  # try this first; or extract IV from ciphertext
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)