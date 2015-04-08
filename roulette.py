import random
from sys import exit
import os

# function for straight bet type
def straight(bank, betType):
    print "You play straight! Please enter your bets: "
    while True:
        amount = raw_input("I play EUR: ")
        if amount.isdigit():
            amount = float(amount)
            if bank - amount >= 0:
                bet = raw_input("{} EUR on number: ".format(amount))
                if bet.isdigit():
                    bet = int(bet)
                    if 0 <= bet <= 36:
                        print "{} EUR on {}. No more bets please!".format(amount, bet)
                        rnd = spinRoulette()
                        if rnd == bet:
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    else:
                        print "invalid bet... try again!"
                else:
                    print "invalid bet..."
            else:
                print "Irregular Bet! Bank Account: {} EUR".format(bank)
        else:
            print "invalid bet..."

# function for first half [1-18] or second [19-36] half bet type
def manque_ou_passe(bank, betType):
    print "You play Manque ou Passe! Please enter your bets: "
    while True:
        amount = raw_input("I play EUR: ")
        if amount.isdigit():
            amount = float(amount)
            if bank - amount >= 0:
                bet = raw_input("{} EUR on (1)Manque or (2)Passe?: ".format(amount))
                if bet.isdigit():
                    bet = int(bet);
                    if bet == 1:
                        print "{} EUR on Manque. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if 1 <= rnd <= 18:
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    elif bet == 2:
                        print "{} EUR on Passe. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if 19 <= rnd <= 36:
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    else:
                        print "invalid choice..."
                else:
                    print "invalid bet..."
            else:
                print "Irregular Bet! Bank Account: {} EUR".format(bank)
        else:
            print "invalid bet..."

# function for black or red bet type
def rouge_ou_noir(bank, betType):
    print "You play Rouge ou Noir! Please enter your bets: "
    while True:
        amount = raw_input("I play EUR: ")
        if amount.isdigit():
            amount = float(amount)
            if bank - amount >= 0:
                bet = raw_input("{} EUR on (1)Rouge or (2)Noir?: ".format(amount))
                if bet.isdigit():
                    bet = int(bet);
                    if bet == 1:
                        print "{} EUR on Rouge. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if rnd in red:
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    elif bet == 2:
                        print "{} EUR on Black. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if rnd in black:
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    else:
                        print "invalid choice..."
                else:
                    print "invalid bet..."
            else:
                print "Irregular Bet! Bank Account: {} EUR".format(bank)
        else:
            print "invalid bet..."

# function for odd or even bet type
def pair_ou_impair(bank, betType):
    print "You play Pair ou Impair! Please enter your bets: "
    while True:
        amount = raw_input("I play EUR: ")
        if amount.isdigit():
            amount = float(amount)
            if bank - amount >= 0:
                bet = raw_input("{} EUR on (1)Pair or (2)Impair?: ".format(amount))
                if bet.isdigit():
                    bet = int(bet);
                    if bet == 1:
                        print "{} EUR on Pair. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if rnd % 2 == 0:
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    elif bet == 2:
                        print "{} EUR on Impair. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if rnd % 2 == 0:
                            return loss(bank, amount)
                        else:
                            return win(bank, amount, betType)
                    else:
                        print "invalid choice..."
                else:
                    print "invalid bet..."
            else:
                print "Irregular Bet! Bank Account: {} EUR".format(bank)
        else:
            print "invalid bet..."

# function for dozen bet type ([1-12] [13-24] [25-36])
def dozen_bets(bank, betType):
    print "You play Dozen Bets! Please enter your bets: "
    while True:
        amount = raw_input("I play EUR: ")
        if amount.isdigit():
            amount = float(amount)
            if bank - amount >= 0:
                bet = raw_input("{} EUR on (1)First, (2)Second or (3)Third Dozen?: ".format(amount))
                if bet.isdigit():
                    bet = int(bet);
                    if bet == 1:
                        print "{} EUR on First Dozen. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if 1 <= rnd <= 12:
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    elif bet == 2:
                        print "{} EUR on Second. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if 13 <= rnd <= 24:
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    elif bet == 3:
                        print "{} EUR on Third Dozen. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if 25 <= rnd <= 36:
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    else:
                        print "invalid choice..."
                else:
                    print "invalid bet..."
            else:
                print "Irregular Bet! Bank Account: {} EUR".format(bank)
        else:
            print "invalid bet..."

# function for column bet type (first, second or third column)
def column_bets(bank, betType):
    print "You play Column Bets! {} please enter your bets: ".format(player)
    while True:
        amount = raw_input("I play EUR: ")
        if amount.isdigit():
            amount = float(amount)
            if bank - amount >= 0:
                bet = raw_input("{} EUR on (1)First, (2)Second or (3)Third Column?: ".format(amount))
                if bet.isdigit():
                    bet = int(bet);
                    if bet == 1:
                        print "{} EUR on First Column. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if rnd in range(1, 37, 3):
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    elif bet == 2:
                        print "{} EUR on Second Column. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if rnd in range(2, 37, 3):
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    elif bet == 3:
                        print "{} EUR on Third Column. No more bets please!".format(amount)
                        rnd = spinRoulette()
                        if rnd in range(3, 37, 3):
                            return win(bank, amount, betType)
                        else:
                            return loss(bank, amount)
                    else:
                        print "invalid choice..."
                else:
                    print "invalid bet..."
            else:
                print "Irregular Bet! Bank Account: {} EUR".format(bank)
        else:
            print "invalid bet..."

# function for spinning the roulette and return the number with color
def spinRoulette():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Roulette spinning....\nand it is: "
    rnd = random.randint(0,36)
    if rnd in red:
        print "[{} Red]".format(rnd)
    if rnd in black:
        print "[{} Black]".format(rnd)
    return rnd

# function for calculating the winning amount according to the bet type and adding to the bank
def win(bank, amount, betType):
    if betType == 1:
        result = amount * 35 # straight
    elif 2 <= betType <= 4:
        result = amount # bet type manque/passe - red/black - even/odd
    else:
        result = amount * 2 # column - dozen bets

    print "You win {} EUR".format(result)
    bank += result
    print "New bank acount: {} EUR\n".format(bank)
    return bank

# function for subtracting the loosing amount from the bank account
def loss(bank, amount):
    print "You Lose {} EUR".format(amount)
    bank -= amount
    print "New bank account: {} EUR\n".format(bank)
    return bank

# function for printing rules and information about the different bet types
def helpme(*args):
    print """
    *** Roulette Guide ***
    (1) Straight (or Single) a bet on a single number [35 to 1]
    (2) Manque (1 to 18) a bet on one of the first 18 numbers. [1 to 1]
        or Passe (19 to 36) a bet on the high 18 numbers. [1 to 1]
    (3) Red or Black (Rouge ou Noir) a bet on which color the roulette wheel
        will show. [1 to 1]
    (4) Even or odd (Pair ou Impair) a bet on even or odd nonzero number.
        [1 to 1]
    (5) Dozen Bets a bet on the first 12 (1-12), second 12 (13-24) or third 12
        (25-36) numbers. [2 to 1]
    (6) Column Bets a bet on one of the three vertical lines e.g.: 1-4-7-10-..
        [2 to 1]

    The numbers in [] represent the payout of each bet e.g. [2 to 1] means
    that you get 2 times the amount you bet from the bank.

    Good Luck!
    """
    return

# use dictionary as data structure
d = {1 : straight, 2 : manque_ou_passe, 3 : rouge_ou_noir,  4 : pair_ou_impair, 5 : dozen_bets, 6 : column_bets, 8 : helpme}
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

### Here the programm starts ###

""" Name input """
os.system('cls' if os.name == 'nt' else 'clear')
print "*** Welcome to Group 7 Roulette ***"
player = None
while True:
    player = raw_input("Please enter your name: ")

    if (player.isalpha()) & (len(player) > 0):
        break
    else:
        print "{} is not a name...".format(player)
print "Hi {}!".format(player)
money = None

""" Money input """
while True:
    print "How much money do you want to bring to a Roulette table?"
    money = raw_input("EUR: ")

    if money.isdigit():
        money = float(money)

        if money > 0:
            print "Your Bank Account: {:.1f} EUR".format(money)
            break
        else:
            print "{} is not a valid amount...".format(money)
    else:
        print "{} is not a valid amount".format(money)

print """
 *** Please choose your bet type ***
(1)Straight
(2)Manque ou Passe
(3)Rouge ou Noir
(4)Pair ou Impair
(5)Dozen Bets
(6)Column Bets

(7)Exit
(8)Help
"""

""" Gameplay logic starts here """
bet_type = None # save bet type
func = None # save function call
while True:
    if money == 0:
        print "You have no more money to play! See you again {}!".format(player)
        exit()
    bet_type = raw_input("What bet type would you like to play? ")
    if bet_type.isdigit():
        bet_type = int(bet_type)
        if 1 <= bet_type <= 6: # call the right function according to bet type
            func = d[bet_type]
            money = func(money, bet_type) # return updated amount of money after each bet
        elif bet_type == 7: # exit roulette terminal
            print "Byebye {}! You leave the roulette table with {:.1f} EUR".format(player, money)
            exit() # terminate application
        elif bet_type == 8: # call helpme() function if bet type is 8
            func = d[bet_type]
            func()
        else:
            print "Invalid bet type! (8) for help\n"
    else:
        print "Invalid bet type! (8) for help\n"
