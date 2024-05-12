def fibo():
    d= int(input("how many numbers you want to print : "))
    n=d
    a = 0
    b=1
    if n==0:
        print(a)
    elif n==1:
        print(b)
    
    elif n<0:
        print("Enter positive number!!!!!")

    else:
            print(a)
            print(b)
            for i in range(2,n):
                c=a+b
                a=b
                b=c
            
                print(c)



fibo()

print("Over")