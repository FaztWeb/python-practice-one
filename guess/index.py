import random

guessesTaken = 0
minNumber = 1
maxNumber = 40

# User Input
print("Hello! What is your name?")
username = input()

number = random.randint(1, 20)
print("Well, " + username + ", I am Thinking of a number between "+ str(minNumber) +" and " + str(maxNumber))

# Loop Game
while guessesTaken < 6:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low.")
    
    if guess > number:
        print("Your guess is too high.")
    
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("God Job, " + username + "! You guessed my Number in " + guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print("No. The number I was thinking of was " + number)