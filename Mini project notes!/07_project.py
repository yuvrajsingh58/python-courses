secret_number = 7

guess = int(input("Guess the number: "))

if guess == secret_number:
    print("Correct Guess")

elif guess < secret_number:
    print("Too Low!")

else:
    print("Too High!")