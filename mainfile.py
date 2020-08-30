import colorsys
print("\u001b[34m       _____ _____ _____  _    _ ______ _____")
print("\u001b[34m	  / ____|_   _|  __ \| |  | |  ____|  __ \ ")
print("	\u001b[34m | |      | | | |__) | |__| | |__  | |__) |")
print("	\u001b[34m | |      | | |  ___/|  __  |  __| |  _  / ")
print("\u001b[34m	 | |____ _| |_| |    | |  | | |____| | \ \ ")
print("	\u001b[34m  \_____|_____|_|    |_|  |_|______|_|  \_\ ")
print(" \u001b[34m        Ｅｎｃｒｙｐｔｏｒ ａｎｄ Ｄｅｃｒｙｐｔｏｒ 𝟷.𝟶       ")
print("  \u001b[33m                                   -ᵃᵗʰᵉˢʰ ᵖᵃʳᵍᵃᵘ⁷")
print("\u001b[31m--------------------------------------------------")
print("\u001b[37m1.Reverse Cipher\n2.Caeser Cipher\n3.ROT13 Cipher\n4.Polybius Square Cipher\n5.Affine Cipher\n6.Atbash Cipher")
print("\u001b[31m----------------------------------------------------\u001b[31m")

def mainsec():
    print("\u001b[31m--------------------------------------------------")
    print(
        "\u001b[37m1.Reverse Cipher\n2.Caeser Cipher\n3.ROT13 Cipher\n4.Polybius Square Cipher\n5.Affine Cipher\n6.Atbash Cipher")
    print("\u001b[31m----------------------------------------------------\u001b[31m")
    mainkey = input("\u001b[0m Enter Your Choice [+] ")
    if mainkey == "1" or (mainkey == "reverse cipher" or mainkey == "Reverse Cipher"):
        revcipher()
    elif mainkey == "2" or (mainkey == "caeser cipher" or mainkey == "Caeser Cipher"):
        caesercipher()
    elif mainkey == "3" or (mainkey == "rot13 cipher" or mainkey == "ROT13 Cipher"):
        rot13()
    elif mainkey == "4" or (mainkey == "Polybius Square Cipher" or mainkey == "polybius square cipher"):
        polybiussquare()
    elif mainkey == "5" or (mainkey == "Affine Cipher" or mainkey == "affine cipher"):
        affineciph()
    elif mainkey == "6" or (mainkey == "Atbash Cipher" or mainkey == "atbash cipher"):
        atbashciph()
    else:
        print("\u001b[31mInvalid Input")
        qn1=input("Do Want to exit [Y/N] ")
        if qn1 == "y" or qn1 =="Y":
            print("Exit[0]")
        elif qn1 =="n" or qn1 =="N":
            mainsec()
        else:
            print("exit")

def revcipher():
    print("Reverse Cipher is selected")
    print("\n1.Encrpyt\n2.Decrypt")
    a = input("enter your choice[1/2] ")
    if a == "1":
        message = input("Enter the plain text: ")
        translate = ""
        x = len(message) - 1
        while x >= 0:
            translate += message[x]
            x = x - 1
        print("encrypting...............")
        print("The reverse cipher of given text is:", translate)
        qn1 = input("Do you want to continue[Y/N] ")
        if qn1 == "y" or qn1 == "Y":
            revcipher()
        else:
            mainsec()
    elif a == "2":
        message = input("Enter the plain text: ")
        translate = ""
        x = len(message) - 1
        while x >= 0:
            translate += message[x]
            x = x - 1
        print("decrypting...............")
        print("The reverse cipher of given text is:", translate)
        qn1 = input("Do you want to continue[Y/N] ")
        if qn1 == "y" or qn1 == "Y":
            revcipher()
        else:
            mainsec()
    else:
        print("\u001b[31m Invalid Input")
        mainsec()

def caesercipher():
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
             'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
             'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
             'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
             'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    dict2 = {0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
             6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
             11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
             16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
             21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y'}

    def encrypt(message, shift):
        cipher = ''
        for letter in message:
            if (letter != ' '):
                num = (dict1[letter] + shift) % 26
                cipher += dict2[num]
            else:
                cipher += ' '

        return cipher

    def decrypt(message, shift):
        decipher = ''
        for letter in message:
            if (letter != ' '):
                num = (dict1[letter] - shift + 26) % 26
                decipher += dict2[num]
            else:
                decipher += ' '

        return decipher

    def maincaeser():
        print('Caeser Cipher is selected')
        print("\n1.Encrypt\n2.Decrypt")
        ankey = input("Enter your choice[1/2] ")
        if ankey == "1":
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter key>> "))
            print("Encrypting......")
            result = encrypt(message, shift)
            print(result)
            qn1 = input("Do you want to continue[Y/N] ")
            if qn1 == "y" or qn1 == "Y":
                maincaeser()
            else:
                mainsec()


        elif ankey == "2":
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter key>>"))
            print("Decrypting......")
            result = decrypt(message, shift)
            print(result)
            qn1 = input("Do you want to continue[Y/N] ")
            if qn1 == "y" or qn1 == "Y":
                maincaeser()
            else:
                mainsec()

        else:
            print("Invalid Input")
            mainsec()

    maincaeser()

def rot13():
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
             'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
             'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
             'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
             'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    dict2 = {0: 'z', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
             6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
             11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
             16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
             21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y'}

    def encrypt(message, shift):
        cipher = ''
        for letter in message:
            if (letter != ' '):
                num = (dict1[letter] + shift) % 26
                cipher += dict2[num]
            else:
                cipher += ' '

        return cipher

    def decrypt(message, shift):
        decipher = ''
        for letter in message:
            if (letter != ' '):
                num = (dict1[letter] - shift + 26) % 26
                decipher += dict2[num]
            else:
                decipher += ' '

        return decipher

    def mainrot():
        print('ROT13 is selected')
        print("\n1.Encrypt\n2.Decrypt")
        ankey = input("Enter your choice[1/2] ")
        if ankey == "1":
            message = input("Enter message to decrypt: ")
            shift = 13
            print("Encrypting......")
            result = encrypt(message, shift)
            print(result)
            qn1 = input("Do you want to continue[Y/N] ")
            if qn1 == "y" or qn1 == "Y":
                mainrot()
            else:
                mainsec()


        elif ankey == "2":
            message = input("Enter message to encrypt: ")
            shift = 13
            print("Decrypting......")
            result = decrypt(message, shift)
            print(result)
            qn1 = input("Do you want to continue[Y/N] ")
            if qn1 == "y" or qn1 == "Y":
                mainrot()
            else:
                mainsec()

        else:
            print("Invalid Input")
            mainsec()

    mainrot()

def polybiussquare():
    def polyencrypt(s):
        for char in s:
            row = int((ord(char) - ord('a')) / 5) + 1
            col = ((ord(char) - ord('a')) % 5) + 1
            if char == 'k':
                row = row - 1
                col = 5 - col + 1

            elif ord(char) >= ord('j'):
                if col == 1:
                    col = 6
                    row = row - 1
                col = col - 1
            print(row, col, end='', sep='')

    def polydecrypt(s):
        for char in s:
            row = chr((ord(char) + ord('a')) / 5) - 1
            col = ((ord(char) + ord('a')) % 5) - 1
            if char == 'k':
                row = row + 1
                col = 5 + col - 1

            elif ord(char) >= ord('j'):
                if col == 1:
                    col = 6
                    row = row + 1
                col = col + 1
            print(row, col, end='', sep='')

    def mainpoly():
        print("Polybius Square Cipher is selected")
        print("\n1.Decryption")
        pskey = input("Enter your choice[1/2] ")
        if pskey == "1":
            s = input("Enter the message ")
            polyencrypt(s)
            qn1 = input("\nDo you want to Continue[Y/N] ")
            if qn1 == "Y" or qn1 == "y":
                mainpoly()
            else:
                mainsec()

        #elif pskey == "2":
            #s = input("Enter the message ")
            #polydecrypt(s)
            #qn1 = input("\nDo you want to Continue[Y/N] ")
            #if qn1 == "Y" or qn1 == "y":
                #mainpoly()
            #else:
               #mainsec()

        else:
            print("Invalid Input")
            mainsec()

    mainpoly()

def affineciph():
    def egcd(a, b):
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b // a, b % a
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        gcd = b
        return gcd, x, y

    def modinv(a, m):
        gcd, x, y = egcd(a, m)
        if gcd != 1:
            return None
        else:
            return x % m

    def encrypt(text, key):
        # E = (a*x + b) % 26
        return ''.join(
            [chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])

    def decrypt(cipher, key):
        # D(E) = (a^-1 * (E - b)) % 26
        return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])

    def mainaffine():
        print("Affine Cipher is selected")
        print("\t\t\t\t\t\n1.Encryption\t\t\t\t\t\n2.Decryption")
        afin = input("Enter your choice[1/2] ")
        if afin == "1":
            text = input("Enter the message: ")
            key = [7, 2]
            enc_text = encrypt(text, key)
            print('Encrypted Text: {}'.format(enc_text))
            afqn = input("Do you want to continue[Y/N] ")
            if afqn == "y" or afqn == "Y":
                mainaffine()
            else:
                mainsec()

        elif afin == "2":
            text = input("Enter the message: ")
            key = [7, 2]
            enc_text = decrypt(text, key)
            print('Decrypted Text: {}'.format(enc_text, key))
            afqn = input("Do you want to continue[Y/N] ")
            if afqn == "y" or afqn == "Y":
                mainaffine()
            else:
                mainsec()

        else:
            print("Invalid Input")
            mainsec()

    mainaffine()

def atbashciph():
    lookup_table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
                    'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
                    'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
                    'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
                    'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}

    def atbash(message):
        cipher = ''
        for letter in message:
            if (letter != ' '):
                cipher += lookup_table[letter]
            else:
                cipher += ' '

        return cipher

    def mainatbash():
        print("Atbash Cipher is selected")
        print("\n1.Encrypt\n2.Decrypt")
        ankey = input("Enter your choice[1/2] ")
        if ankey == "1":
            message = input("Enter message to Encrypt: ")
            print(atbash(message.upper()))
            qn1 = input("Do you want to continue[Y/N] ")
            if qn1 == "y" or qn1 == "Y":
                mainatbash()
            else:
                mainsec()
        elif ankey == "2":
            message = input("Enter message to Decrypt: ")
            print(atbash(message.upper()))
            qn1 = input("Do you want to continue[Y/N] ")
            if qn1 == "y" or qn1 == "Y":
                mainatbash()
            else:
                mainsec()
        else:
            print("Invalid Input")
            mainsec()

    mainatbash()

mainkey=input("\u001b[0m Enter Your Choice [+] ")
if mainkey == "1" or (mainkey =="reverse cipher" or mainkey =="Reverse Cipher"):
    revcipher()
elif mainkey =="2" or (mainkey =="caeser cipher" or mainkey == "Caeser Cipher"):
    caesercipher()
elif mainkey == "3" or (mainkey =="rot13 cipher" or mainkey == "ROT13 Cipher"):
    rot13()
elif mainkey == "4" or (mainkey == "Polybius Square Cipher" or mainkey =="polybius square cipher"):
    polybiussquare()
elif mainkey =="5" or (mainkey == "Affine Cipher" or mainkey=="affine cipher"):
    affineciph()
elif mainkey=="6" or (mainkey =="Atbash Cipher" or mainkey=="atbash cipher"):
    atbashciph()
else:
    print("\u001b[31mInvalid Input")
    qn1 = input("Do Want to exit [Y/N] ")
    if qn1 == "y" or qn1 == "Y":
        print("Exit[0]")
    elif qn1 == "n" or qn1 == "N":
        mainsec()
    else:
        print("exit")


