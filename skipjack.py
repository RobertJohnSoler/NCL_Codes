from skipjack import Skipjack
key_bytes = bytes.fromhex("6578706C6F697420696E")  # your 10-byte key
skj = Skipjack(key_bytes)

# assume ECB:
ct = bytes.fromhex("9e59eae1fe064a3a     275596d5bdbe655c")    # your ciphertext
pt = bytearray()
for i in range(0, len(ct), 8):
    pt += skj.decrypt_block(ct[i:i+8])
print(pt)