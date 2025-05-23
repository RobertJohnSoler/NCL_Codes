#!/usr/bin/env python2.7

import sys

def verify(submission):
    # print(submission)
    processed = [ ]
    if len(submission) % 2 != 0:
        return False

    for i in range(0, len(submission) // 2):
        processed.append(int(submission[i * 2] + submission[(i * 2) + 1], 16))

    ekc = [ 0x53, 75, 0x59, 0x2D, 110, 0x45, 88, 72, 0x2D, 0x35, 0x36, 0x38, 0x30 ]
    if len(processed) != len(ekc):
        # print(len(processed), len(ekc))
        return False

    for i in range(len(processed)):
        if ekc[i] != processed[i]:
            # print(ekc[i], processed[i])
            return False

    return True

# if len(sys.argv) != 1:
#     print ("Usage: python bytes.pyc")
#     exit(1)

# submission = input("What is the password? ")
# print(type(len(submission)))
# if verify(submission):
#     print ("That is correct")
#     exit(0)
# else:
#     print ("That is incorrect")
#     exit(2)

i = 1
while True:
    submission = str(i).zfill(26)
    status = verify(submission)
    if status:
        print(submission, status)
        break
    i+=1