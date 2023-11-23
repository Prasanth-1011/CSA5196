a = []
for i in range(65,91):
    a.append(chr(i))

k = input("Enter Key : ")    
p = input("Enter Plain Text : ")
b = []
c = ''
k = k.upper()
p = p.upper()

for i in k:
    if i not in b:
        b.append(i)
for i in a:
    if i not in b:
        b.append(i)
        
print("\n",a)
print("\n",b)

for i in p:
    e = a.index(i)
    c = c+b[e]
print("Encrypted Cipher Text : "+c)

m = ''
for i in c:
    e = a.index(i)
    m = m+b[e]
print("Decrypted Plain Text : "+c)
