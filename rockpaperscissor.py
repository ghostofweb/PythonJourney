rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random

def game():
    print("Welcome to the game of rock, paper, and scissors!")
    
    while True:
        user_choice = int(input("What do you choose? 1 for rock, 2 for paper, 3 for scissors: "))
        choices = [rock, paper, scissor]
        print("You chose:")
        print(choices[user_choice - 1])
        
        cpu_choice = random.randint(1, 3)
        print("Computer chose:")
        print(choices[cpu_choice - 1])

        if user_choice == cpu_choice:
            print("It's a draw!")
        elif (user_choice == 1 and cpu_choice == 3) or \
             (user_choice == 2 and cpu_choice == 1) or \
             (user_choice == 3 and cpu_choice == 2):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("thanks for playing")
            break

game()