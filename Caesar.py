import string
#A caesar cypher that accepts lowercase letters
def caesar(message,key,direction):

#disc will be used to store the alphabet following a shift 
    disc={}
    alphabet = string.ascii_lowercase

#direction used to determine if encrypting or decrypting 
    if direction == 0:
        for n in range(0, 26):
            disc[alphabet[n]] = alphabet[(n+key)%26]
    elif direction == 1:
        for n in range(0, 26):
            disc[alphabet[n]] = alphabet[(n-key)%26]

#The code is processed into a string 
    code=""

    for i in message.lower():
        if i in disc:
            i=disc[i]
        code+=i
        
    return code


def user_input():
    print('Would you like to encrypt(1), decrypt(2), or quit(3)?')

while True:
    user_input()
    userChoice = int(input('Enter 1, 2, or 3: ' ))
    if userChoice == 1:
        direction = 0
        message = input('Type the message you would like encrypted: ')
        key = int(input('Type a key for the cipher: '))
        print(caesar(message,key,direction))
    elif userChoice == 2:
        direction = 1
        message = input('Type the letters you would like decrypted: ')
        key = int(input('Type a key for the cipher: '))
        print(caesar(message,key,direction))
    elif userChoice == 3:
        break
