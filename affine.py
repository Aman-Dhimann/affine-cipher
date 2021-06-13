import sys
stri = input("enter a string")
print(stri)
key = int(input("enter the key"))
key2 = int(input("enter the key"))
encrypted = str("")
decrypted = str("")
for i in stri:
    if i.isupper():
        encrypted += (chr(((((ord(i)-65)*key)+key2) % 26)+65))
    else:
        encrypted += (chr(((((ord(i)-97)*key)+key2) % 26)+97))

r = int(0)
q = int(0)
r1 = int(26)
r2 = int(key)
t1 = int(0)
t2 = int(1)
while r2 != 0:
    r = r1 % r2
    q = r1 / r2
    r1 = r2
    r2 = r
    t = t1-(q*t2)
    t1 = t2
    t2 = t
if r1 == 1:
    key_inv = int(t1)
else:
    print("key inverse doesn't exist")
    sys.exit()
print("encrypted cipher is "+encrypted)
for i in encrypted:
    if i.isupper():
        decrypted += (chr(((((ord(i)-65)-key2)*key_inv) % 26)+65))
    else:
        decrypted += (chr(((((ord(i)-97)-key2)*key_inv) % 26)+97))
print("decrypted cipher is " + decrypted)