builder = 12645638
ord_password = 78
len_password = 11
password = ""

builder = ~builder
builder = builder ^ 12648430
builder = ~builder
builder = builder >> 2


print(builder)  # 698
print(chr(62))  # >
print("N>>>>>>>>>>")