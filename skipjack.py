from skipjack import Skipjack
key_bytes = bytes.fromhex("0123456789ABCDEFF0")  # your 10-byte key
skj = Skipjack(key_bytes)

# assume ECB:
ct = bytes.fromhex("…")    # your ciphertext
pt = bytearray()
for i in range(0, len(ct), 8):
    pt += skj.decrypt_block(ct[i:i+8])
print(pt)