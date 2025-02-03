import sys

# def main():
#     if len(sys.argv) != 2:
#         print ('Invalid args')
#         return
#     password = sys.argv[1]
#     counter = 0
#     vals = list('tfzbwlyzljylawhzzdvyk')
#     if len(password) != len(vals):
#         print ('incorrect')
#         return
#     while counter < len(password):
#         x = ord(password[counter]) + 7
#         if x > ord('z'):
#             x -= 26
#         if chr(x) != vals[counter]:
#             print ('incorrect')
#             return
#         counter += 1

#     print ('correct')


def main():
    vals = list('tfzbwlyzljylawhzzdvyk')
    password = ""
    counter = 0
    while counter < len(vals):
        v = vals[counter]
        x = ord(v)
        if x > ord('z'):
            x += 26
        x = x-7
        c = chr(x)
        password = password+c
        print(password)
        counter+=1

if __name__ == '__main__':
    main()