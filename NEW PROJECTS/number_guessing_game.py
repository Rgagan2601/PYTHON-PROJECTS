import random

jackpot = random.randint(1,100)

guess = int(input("Enter the number : "))
count = 1
while(guess != jackpot):
    if guess < jackpot:
        print("guess higher ")
    else:
        print("guess lower ")
    guess = int(input("Enter the number : "))
    count +=1
print("you guessed correctly")
print("in",count)

