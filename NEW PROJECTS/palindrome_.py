# def palin(Text):
#     if len(Text) <=1:
#         print("palindrome")
#     elif Text[0]==Text[-1]:
#         palin(Text[1:-1])
#     else:
#         print("not a palindrome")
# palin("madam")
# palin("malayalam")
# palin("python")

#-----------------------------------------------------------------------------------------

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(24))
