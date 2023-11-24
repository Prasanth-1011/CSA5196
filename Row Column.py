import math
n = input("Enter the Key : ")
p = input("Enter the Plain Text : ")
col = len(n)
row = math.ceil(len(p)/col)

b = [[0 for _ in range(col)] for _ in range(row)]
m = 0

for i in range(row):
    for j in range(col):
        b[i][j] = p[m]
        m += 1
        if m == len(p):
            break
        
for i in range(row):
    for j in range(col):
        if b[i][j] == 0:
            b[i][j] = 'X'
            
c = ""
for i in n:
    for j in range(row):
        c += b[j][int(i)-1]
print("Cipher Text : ",c)
