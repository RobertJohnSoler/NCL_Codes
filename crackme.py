# First 8 bytes of encoded_image from your screenshot
encoded_image = [0x41, 0xEF, 0xD6, 0x16, 0xDA, 0xD7, 0xE3, 0xE9]

# Standard PNG file header (in hex)
png_header = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]

# Compute key: key[i] = png_header[i] - encoded_image[i]
key = [(png_header[i] - encoded_image[i]) % 256 for i in range(8)]

# Print the key as characters (or bytes if it's not printable)
print("param_1 as bytes:", key)
print("param_1 as string:", ''.join(chr(b) if 32 <= b <= 126 else '.' for b in key))