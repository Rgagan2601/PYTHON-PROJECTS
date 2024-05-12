n = 1
def factorial_recursive(n):
    if n ==1:
        return 1
    else:
       return n*factorial_recursive(n-1)

nb  = int(input("Enter the number : \n"))

print(factorial_recursive(nb))