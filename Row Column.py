import math
n = input("Enter the Key : ")
p = input("Enter the Plain Text : ")
col = len(n)
row = math.ceil(len(p)/col)

b = [['X' for _ in range(col)] for _ in range(row)]
m = 0

for i in range(row):
    for j in range(col):
        b[i][j] = p[m]
        m += 1
        if m == len(p):
            break
            
c = ""
for i in n:
    for j in range(row):
        c += b[j][int(i)-1]
print("Cipher Text : ",c)
