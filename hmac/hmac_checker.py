import hmac
import hashlib

key = b"ciCloud-API-20240315-4f7b9c"
mismatches = 0
stored_hmacs = []

for i in range (1, 51):
    msg = f"messages/message_{i}.txt"
    hMac = f"messages/message_{i}.hmac"
    with open(msg, "r") as msg_file, open(hMac) as hmac_file:
        msg_content = msg_file.read()
        hmac_content = hmac_file.read()
        h = hmac.new(key, bytes(msg_content, 'utf-8'), hashlib.sha256)
        signature = h.hexdigest()
        print("Results for "+ msg + ":")
        print("Hmac file contents: " + hmac_content)
        print("Calculated signature: "+ signature)
        if hmac_content != signature:
            print("Mismatch found!")
            mismatches = mismatches + 1
        else:
            pass
        if signature in stored_hmacs:
            print(f"Found reused hmac in {msg}!")
        stored_hmacs.append(hmac_content)

print("\nMismatches:", mismatches)
