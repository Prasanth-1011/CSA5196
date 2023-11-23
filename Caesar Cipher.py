Array = []
for i in range(65,91):
    Array.append(chr(i))

Input = input("Enter Plain Text : ") # Input Cipher Text For Decryption
Upper = Input.upper()

for Key in range(1,26):
    Cipher = ''
    # Plain = ''
    
    for i in Upper:
        if(i == ' '):
            Cipher = Cipher + ' '
            # Plain = Plain + ' '
        else:
            Index = Array.index(i)
            Encrypt = (Index + Key) % 26
            # Decrypt = (Index - Key) % 26
            Cipher = Cipher + Array[Encrypt]
            # Plain = Plain + Array[Decrypt]
    
    print("Encrypted Cipher Text When Key Value {0} : {1}".format(Key, Cipher))
    
