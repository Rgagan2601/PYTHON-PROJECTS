#FAULTY CALCULATOR
#45*3 = 555, 56+9=77 , 56/6 = 4

num1 = int(input("Enter number 1 : "))
num2= int(input("Enter number 2 : "))

op = input("Enter operator : "
           "+ = addition "
           "\n- = substraction "
           "\n* = multiplication "
           "\n/ = division\n"
           "% for modulo\n")

if num1==45 and num2 == 3 and op=='*':
    print("555")
elif num1 == 56 and num2 == 9 and op == '+':
    print("77")
elif num1 == 56 and num2 == 6 and op == '/':
    print("4")

elif op == '+':
    print(num2+num1)
elif op == '*':
    print(num2*num1)
elif op == '/':
    print(num2/num1)
elif op == '-':
    print(num2-num1)
elif op == '%':
    print(num2%num1)

else:
    print("choose given operator only !")


