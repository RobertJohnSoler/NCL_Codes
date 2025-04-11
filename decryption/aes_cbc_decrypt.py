from Crypto.Cipher import AES
import hashlib

# Read the ciphertext from file
with open("ciphertext", "rb") as f:
    ciphertext = f.read()

start_timestamp = 1672531200   # 2023-01-01 00:00:00 UTC
end_timestamp   = 1672617600   # 2023-01-02 00:00:00 UTC

for t in range(start_timestamp, end_timestamp):
    # 1) Derive a 16-byte key using MD5 of the string representation of the timestamp
    key = hashlib.md5(str(t).encode()).digest()  # 128 bits

    # 2) Let's guess the IV is all zeros first...
    iv = b"\x00" * 16

    # 3) Decrypt
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = cipher.decrypt(ciphertext)

    # 4) Check if the plaintext is readable or has a flag
    if b"SKY" in plaintext:
        print(f"[+] Found a promising timestamp: {t}")
        print("[+] Potential plaintext:")
        print(plaintext)
        # print(plaintext.decode("utf-8"))
        # break
