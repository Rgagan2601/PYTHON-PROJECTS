#printing pascals triangle

row = int(input("Enter the no of rows : "))

for i in range(0,row+1):
    for j in range(0,i):
        print(" * ",end="")
    print()

