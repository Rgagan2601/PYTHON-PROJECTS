# printing star pattern=======using loop

print("How many row you want to print : ")
row1 = int(input())
print("Type 1 or 0 : ")
two = int(input())

# if two == 1:
#
#     for i in range (0,row1,+1) :
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
#
# elif two == 0:
#     for i in range (row1,0,-1):
#         for j in range (1,0,i-1):
#             print("*",end=" ")
#         print()

# if two == 1:
#     count = 0
#     while(count<row1):
#         print(" * "* count,end="")
#         print()
#         count = count+1

# elif two == 0:
#     count = row1
#     while(count>0):
#         print(" * "* count,end="")
#         print("\n",end="")
#         count=count-1
if two == 1:
    # for i in range(0,row1,+1):
    #     for j in range(1,i+1):
    #      print("*",end=" ")
    # print()

    for i in range(0, row1, +1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

elif two == 0:
    for i in range(row1,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()