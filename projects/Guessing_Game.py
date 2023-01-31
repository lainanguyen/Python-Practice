secret_number = 9
guess_count = 0
guess_limit = 3

print("Welcome to the guessing game!")
print("You have 3 tries to guess the secret number")
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You win!")
        break
else:
    print("Sorry, you failed!")


