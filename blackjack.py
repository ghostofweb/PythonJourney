
import random

usergame = 1
mpgame = 1

def ran():
    """Generates a random card value between 1 and 10."""
    return random.randint(1, 10)

def checkforuser(score, user, comp):
    """Checks if the user score is above 21 and sets flags accordingly."""
    global usergame
    if score <= 21:
        return True
    usergame = 0
    celebrate(user, comp, usergame, compgame)
    return False

def checkforcomp(score, user, comp):
    """Checks if the computer score is above 21 and sets flags accordingly."""
    global compgame
    if score <= 21:
        return True
    compgame = 0
    celebrate(user, comp, usergame, compgame)
    return False


def celebrate(user, comp, usergame, compgame, score=None):
    """Prints final scores and declares winner or tie."""
    print(f"Your final score: {user}, final score: {sum(user)}")
    print(f"Computer final score: {comp}, final score: {sum(comp)}")

    if usergame == 0 and compgame == 0:
        print("TIE")
    elif usergame == 0:
        print("Computer won")
    elif compgame == 0:
        print("You won!")
    else:
        if sum(user) > 21:
            print("You busted! Computer won")
        elif sum(comp) > 21:
            print("Computer busted! You won!")
        else:
            if sum(user) > sum(comp):
                print("You won!")
            elif sum(user) < sum(comp):
                print("Computer won")
            else:
                print("TIE")

def blackjack():
    """Runs the Blackjack game."""
    print("""
    .------.  ,;;,
    |A_    _ ||_ /_
    |( \/ ).-----.
    | \  /|K /\  |
    |  \/ | /  \ |
    `-----| \  / |
            `------'
    """)

    user = [ran(), ran()]
    comp = [ran(), ran()]
    con = True

    while con:
        print(f"Your card: {user}, current score: {sum(user)}")
        print(f"Computer's First card: {comp[0]}")

        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if choice == 'y':
            user.append(ran())
            if sum(user) > 21:
                if not checkforuser(sum(user), user, comp):
                    break
            if random.randint(0, 1) == 1:
                comp.append(ran())
                if sum(comp) > 21:
                    if not checkforcomp(sum(comp), user, comp):
                        break
        elif choice == 'n':
            
            if sum(user) > 21 or sum(comp) > 21:
                celebrate(user, comp, usergame, compgame)
                break
            if not checkforuser(sum(user), user, comp):
                break
            if not checkforcomp(sum(comp), user, comp):
                break
            con = False  # Exit the loop when user chooses 'n'
            celebrate(user, comp, usergame, compgame)  

# Run the game
blackjack()
