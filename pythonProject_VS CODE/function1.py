def is_even(number):
    """     This is a function code 
    created by - Gagan Rajput
    """


    if number%2==0:
        return "even"
    else:
        return "odd"
for i in range(1,11):
    print(is_even(i))
print(is_even.__doc__)