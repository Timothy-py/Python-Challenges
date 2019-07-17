# CAESER CIPHER
msg = input('Enter the message to encode here: ')
cipherMsg = ""

up_msg = msg.upper()

for letter in up_msg:
    if letter == 'Z':
        leta = 'A'
    if letter == ' ' or letter.isdigit() == True:
        continue
    else:
        no = ord(letter)
        no += 1
        leta = chr(no)
    cipherMsg += leta
print(cipherMsg)

'''text = input("Enter message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
print(cipher)'''

