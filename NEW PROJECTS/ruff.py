def sum():

  # print(a+b)
  return a+b

def substract():
    print( a-b)

def mul():
    print(a*b)
def divide():
    if a<b:
        print(a//b)
    else:
        print(a/b)


a = int(input("Value of a "))
b = int(input("Value of b "))


print("\n press 1 for sum\n press 2 for substract\n press 3 for multiply\n press 4 for divide\n ")
inp = int(input())
if inp == 1:
    # print(sum())
    print(sum())
elif inp == 2:
    # print(substract())
    print(substract())
elif inp == 3:
    # print(mul())
    print(mul())
elif inp == 4 :
    # print(divide())
   print( divide())
else :
    print("Enter the correct value!!!!")







