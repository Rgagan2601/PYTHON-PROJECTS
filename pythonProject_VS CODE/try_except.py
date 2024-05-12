print("num1 : ")
num1 = int(input())
print("num2 : ")
num2 = int(input())

try:
    print("sum is : ", num1+num2)
except Exception as e:
    print(e)

print("This line is very important")