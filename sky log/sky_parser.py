from datetime import datetime

logs = []
converted_logs = []
total_bytes = 0

def hex_to_ip(hex_input):
    """
    Convert a hexadecimal input to an IP address string.
    Args:
        hex_input (str): The hexadecimal input to convert.
    Returns:
        str: The corresponding IP address string.
    Example:
        >>> hex_to_ip("C0A80001")
        '192.168.0.1'
    """
    # Convert the hexadecimal input to a decimal integer
    decimal_input = int(hex_input, 16)

    # Convert the decimal input to an IP address string
    ip_address = ".".join(
        map(str, [decimal_input >> 24, (decimal_input >> 16) & 255, (decimal_input >> 8) & 255, decimal_input & 255])
    )

    # Return the IP address string
    return ip_address

with open("sky.txt", "r") as file:
    lines = file.readlines()
    for l in lines:
        row = l.split(" ")
        logs.append(row)

with open("sky.log", "w") as outfile:
    for l in logs:
        src_ip = hex_to_ip(l[0])
        dst_ip = hex_to_ip(l[1])
        timestamp = int(l[2], 16)
        time = datetime.fromtimestamp(timestamp)
        bytes_transferred = int(l[3], 16)
        total_bytes = total_bytes + bytes_transferred
        # print(src_ip, dst_ip, time, bytes_transferred)
        converted_logs.append([src_ip, dst_ip, time, bytes_transferred])
        outfile.write(f"{src_ip} {dst_ip} {time} {bytes_transferred} \n")

print(total_bytes)

ip_data = {}
for l in converted_logs:
    if l[0] not in ip_data:
        ip_data[l[0]] = l[3]
    elif l[0] in ip_data:
        ip_data[l[0]] = ip_data[l[0]] + l[3]
print(ip_data)