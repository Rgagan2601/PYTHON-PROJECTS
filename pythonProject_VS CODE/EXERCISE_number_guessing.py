# Exercise for number guessing

n = 18
no_of_guesses = 0
print("You get limed guesses..so try to guess correctly ")

while (no_of_guesses <= 5):

    print("Guess the number :  ")
    inp = int(input())
    no_of_guesses += 1

    if inp > 18:
        print("You guessed greater number....Please select smaller ")
    elif inp < 18:
        print("You guessed smaller number..Please choose greater ")
    elif inp == 18:
        print("HURRAYYYYYYY...you guessed corectly")
        print("\n you guessed no in ", no_of_guesses, " attemp ")
        break
    else:
        print("please select correct input")
    print("no guesses left : ", 5 - no_of_guesses)
    if no_of_guesses > 4:
        print("GAME OVER..YOU LOST \n")
        break

    # no_of_guesses = no_of_guesses + 1
