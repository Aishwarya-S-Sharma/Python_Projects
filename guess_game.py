import random

correct_guess=random.randint(1,100)

guess=int(input("Guess the correct number : "))

counter=0
while guess!=correct_guess:
    if guess<correct_guess:
        print("Guess a higher number")
    else:
        print("Guess a lower number")

    guess=int(input("Guess the correct number : "))
    counter+=1


print("\nYou guessed it right!")
print(f"You took {counter} attempts to guess.")