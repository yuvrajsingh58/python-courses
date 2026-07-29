import random

secret = random.randint(1, 10)

guess = int(input("Guess a number (1-10): "))

if guess < 1 or guess > 10:
    print("Please enter a number between 1 and 10.")

elif guess == secret:
    print("🎉 Correct! You Win!")

else:
    print("❌ Wrong Guess!")
    print("Correct Number was", secret)