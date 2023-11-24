Depth = int(input("Enter Depth : "))
Plain = input("Enter Plain Text : ")

Rails = ['' for _ in range(Depth)]
dir = 1  # 1 For Down, -1 For Up
row = 0

for i in Plain:
    Rails[row] += i
    row += dir
    if row == 0 or row == Depth - 1:
        dir *= -1

c = ' '.join(Rails)
print("Cipher: " + c)
