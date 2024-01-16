import random

def game():
    lives = 0
    print("Welcome To the Number Guessing Game \n I'm thinking of a number between 1 to 100")
    number = random.randint(1, 100)
    choice = input("Choose the difficulty, Type 'e' for easy(10 lives) or type 'h' for hard(5 lives): ").lower()
    
    if choice == 'e':
        lives = 10
    elif choice == 'h':
        lives = 5
    else:
        print("You chose wrong")

    for i in range(1, lives + 1):
        guess = int(input("Guess the number: "))
        if guess > number:
            print("TOO HIGH")
        elif guess < number:
            print("TOO LOW")
        elif guess == number:
            print(f"You guessed it! The number was {number}")
            break
    else:
        print(f"Sorry, you ran out of lives. The correct number was {number}")

game()
