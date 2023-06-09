initial_text = hello world  #-> catca tcatc -> jeeno pqref
key = cat
initial_text = list(initial_text)
key = list(key)
key_len = len(key)
count = 0
key_text = []
for i in range(len(initial_text)):
    if not 97 <= ord(initial_text[i]) <= 122:
        key_text.append(initial_text[i])
        count += 1
    else:
        key_text.append(key[(i - count) % key_len])
vigenere = 
for i in range(len(initial_text)):
    if not 97 <= ord(initial_text[i]) <= 122:
        char = initial_text[i]
    else:
        char = chr(97 + (ord(initial_text[i]) + ord(key_text[i]) - 97 - 97) % 26)
    vigenere += char
print(vigenere)

/////////////////////////////////////////////////////
import hashlib

def sign_up(file, login, password):
    file.write(login +  :  + password + n)

def sign_in(file, login, password):
    if login +  :  + password in file.read():
        return (Welcomecd vigener !)
    file.seek(0)
    if not login in file.read():
        return (User not found)
    elif not password in file.read():
        return (Password is wrong)

a = int(input())
login = input()
file_a = open(rC:UsersAdminDesktopLogandPass.txt, a)
file_r = open(rC:UsersAdminDesktopLogandPass.txt, r)
password = input()
password = hashlib.sha256(password.encode())
password = password.hexdigest()

if a == 1:
    sign_up(file_a, login, password)
elif a == 2:
    print(sign_in(file_r, login, password))
    
file_a.close()
file_r.close()
