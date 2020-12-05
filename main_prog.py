import random
import time

print("Welcome to Game zone!!")
Bank_amount = int(input("Enter the amount you want to play with(Max amount - 50) : "))

amount = Bank_amount
bet_amount = 0

def highandLow():
    """This function is for running the high and low game"""
    global amount
    while amount != 0:
        """This loop will keep the user playing until their balance is 0 """

        def check():
            """This function will validate the betting amount to check if user has sufficient balance in his bank"""
            global bet_amount
            user_bet = int(input("Please place your betting amount!! : "))
            if user_bet <= amount:
                bet_amount = user_bet
            else:
                print("You are trying to place the bet more than your bank amount! Please try again.")
                return check()
        check()
        time.sleep(1)   #Purposely delaying to make the check function looks like real
        amount = amount - bet_amount
        print(f"Thanks for placing the bet. Your total bet is {bet_amount} Good luck!!")
        choice = int(input("Press 1. for choosing Below 7\n"
                           "Press 2. for choosing Lucky 7\nPress 3. for choosing Above 7\nEnter your choice : "))
        dice_roll = random.randint(1,12)
        print(f"Dice rolled and number came as {dice_roll}")
        if dice_roll == 7 and choice == 2:
            print("Congratulations!! You won!!")
            amount = amount + bet_amount * 3
            print(f"Your new bank amount is {amount}")
            playmore()
        elif dice_roll > 7 and choice == 3:
            print("Congratulations!! You won!!")
            amount = amount + bet_amount * 2
            print(f"Your new bank amount is {amount}")
            playmore()
        elif dice_roll < 7 and choice == 1:
            print("Congratulations!! You won!!")
            amount = amount + bet_amount * 2
            print(f"Your new bank amount is {amount}")
            playmore()
        else:
            print("Bad luck!! You Lost!")
            print(f"Your new bank amount is {amount}")



def snakewatergun():
    """This function is for running the snake water gun game"""
    global amount
    amount = amount - 10

    comp = 0
    user = 0

    print("1. Enter 'w' for choosing 'Water'", "\n2. Enter 's' for 'Snake'", "\n1. Enter 'g' for 'Gun'")
    options = ['Snake', 'Water', 'Gun']
    i = 0
    while i < 9:
        """This loop is for running the game till 9 turns"""
        choose = random.choice(options)
        you = input("Enter your choice : ")
        if you == 'w' and choose == 'Gun':
            print("You sink computer's gun deep inside the water!")
            user = user + 1
        elif you == 'w' and choose == 'Snake':
            print("!! Computer's snake drank your whole water bowl!!")
            comp = comp + 1
        elif you == 'w' and choose == 'Water':
            print("Tie! You both have choose same weapon ")
        elif you == 's' and choose == 'Gun':
            print("!! Computer's Gun shot your poisonous Snake !")
            comp = comp + 1
        elif you == 's' and choose == 'Snake':
            print("Tie! You both have choose same weapon ")
        elif you == 's' and choose == 'Water':
            print("Your poisonous Snake drank whole computer's w!")
            user = user + 1
        elif you == 'g' and choose == 'Gun':
            print("Tie! You both have choose same weapon ")
        elif you == 'g' and choose == 'Snake':
            print("You shot the poisonous snake with your Gun!")
            user = user + 1
        elif you == 'g' and choose == 'Water':
            print("You lost the your gun deep inside the dark sea!")
            comp = comp + 1
        i = i + 1

    if comp > user:
        print(f"Computer Points : {comp}, User Points : {user}")
        print("Bad luck! You lost the game")
    elif user > comp:
        print(f"Computer Points : {comp}, User Points :{user}")
        print("Congratulations! You won the game")
    else:
        print(f"Computer Points : {comp}, User Points :{user}")
        print("Game Drawn!")

    print(f"Your new bank amount is {amount}")
    playmore()


def guessnumber():
    """This function is for running the guess the number game"""
    global amount
    amount = amount - 10

    ans = random.randint(0, 100)
    i = 1
    j = 9
    while i < 9:
        """This loop is for running the game till 9 turns"""
        guess = int(input("Enter your guess : "))
        if guess > ans:
            j = j - 1
            print("Guess too high!")
        elif guess < ans:
            j = j - 1
            print("Guess too low!")
        elif guess == ans:
            print("You have guessed the number correctly in " + str(i) + " attempts")
            break
        i = i + 1
        print("You have " + str(j) + " chances left")
    print(f"Your new bank amount is {amount}")
    playmore()


def gamelist():
    """This function is for displaying the list of games user can play"""
    user_game = int(input("Press 1. Play Lucky 7\nPress 2. Play snake, water and Gun\n"
                      "Press 3. Play guess the number game\nEnter your choice : "))

    if user_game == 1:
        highandLow()
    elif user_game == 2:
        snakewatergun()
    elif user_game == 3:
        guessnumber()


def playmore():
    """This function is for promting the user to play more if they have balance left"""
    if amount > 0:
        user_inp = int(input("Press 1 to play more or 2 to exit :- "))
        if user_inp == 1:
            gamelist()
        else:
            exit()
    else:
        exit()

gamelist()


print("Game Over!!")



