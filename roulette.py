# -*- coding: utf-8 -*-
import random
from sys import exit

# function for straight bet type
def straight(input):
    print "You play straight! Enter your bets: "

    while True:
        amount = raw_input("I play EUR: ")
        if amount.isdigit():
            amount = float(amount)
            if (input - amount >= 0) & (amount >= 0):
                bet = int(raw_input("{} EUR on: ".format(amount)))
                if 0 <= bet <= 36:
                    print "{} EUR on {}. No more bets please!".format(amount, bet)
                    rnd = spinRoulette()

                    if rnd == bet:
                        print "You Win {} EUR".format(amount*35)
                        input += amount * 35
                        print "New bank acount: {} EUR".format(input)
                        return input
                    else:
                        print "You Lose {} EUR".format(amount)
                        input -= amount
                        print "New bank account: {} EUR".format(input)
                        return input
                else:
                    print "invalid bet... try again!"
                    continue
            else:
                print "Irregular Bet! Bank Account: {} EUR".format(input)
        else:
            print "invalid bet..."

    return

# function for Manque or Passe bet type
def manque_ou_passe(input):
    print "You play Manque ou Passe! Enter your bets: "
    while True:
        amount = raw_input("I play EUR: ")
        if amount.isdigit():
            amount = float(amount)
            if input - amount >= 0:
                bet = raw_input("{} EUR on (1)Manque or (2)Passe?: ".format(amount))
                if bet.isdigit():
                    bet = int(bet);
                    if bet == 1:
                        print "{} EUR on Manque. No more bets please!".format(amount)
                        rnd = spinRoulette()

                        if 1 <= rnd <= 18:
                            print "You win {} EUR".format(amount)
                            input += amount
                            print "New bank acount: {} EUR".format(input)
                            return input
                        else:
                            print "You Lose {} EUR".format(amount)
                            input -= amount
                            print "New bank account: {} EUR".format(input)
                            return input

                    elif bet == 2:
                        print "{} EUR on Passe. No more bets please!".format(amount)
                        rnd = spinRoulette()

                        if 19 <= rnd <= 36:
                            print "You win {} EUR".format(amount)
                            input += amount
                            print "New bank acount: {} EUR".format(input)
                            return input
                        else:
                            print "You Lose {} EUR".format(amount)
                            input -= amount
                            print "New bank account: {} EUR".format(input)
                            return input
                    else:
                        print "invalid choice..."
                else:
                    print "invalid bet..."
            else:
                print "Irregular Bet! Bank Account: {} EUR".format(input)
        else:
            print "invalid bet..."
    return

def rouge_ou_noir(input):
    print "rouge ou noir"
    return

def pair_ou_impair(input):
    print "pair_ou_impair"
    return

def dozen_bets(input):
    print "dozen_bets"
    return

def column_bets(input):
    print "column_bets"
    return

# function for spinning the roulette and return the number with color
def spinRoulette():
    rnd = random.randint(0,36)
    if rnd in red:
        print "{} Red".format(rnd)
    if rnd in black:
        print "{} Black".format(rnd)
    return rnd

# function for printing rules and information about the different bet types
def helpme(*args):
    print """
    *** Roulette Guide ***
    (1) Straight (or Single) a bet on a single number [35 to 1]
    (2) Manque (1 to 18) a bet on one of the first 18 numbers. [1 to 1]
        or Passe (19 to 36) a bet on the high 18 numbers. [1 to 1]
    (3) Red or Black (Rouge ou Noir) a bet on which color the roulette wheel will show. [1 to 1]
    (4) Even or odd (Pair ou Impair) a bet on even or odd nonzero number. [1 to 1]
    (5) Dozen Bets a bet on the rst 12 (1-12), second 12 (13-24) or third 12 (25-36) numbers. [2 to 1]
    (6) Column Bets a bet on one of the three vertical lines e.g.: 1-4-7-10 . . . [2 to 1]

    The numbers in [] represent the payout of each bet e.g. [2 to 1] means that you get 2 times
    the amount you bet from the bank. Good Luck!
    """
    return

# use dictionary as data structure
d = {1 : straight, 2 : manque_ou_passe, 3 : rouge_ou_noir,  4 : pair_ou_impair, 5 : dozen_bets, 6 : column_bets, 8 : helpme}
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

### Here the programm starts ###

print "*** Welcome to Group 7 Roulette ***"

player = None
while True:
    player = str(raw_input("Please enter your name: "))

    if (player.isalpha()) & (len(player) > 0):
        break
    else:
        print "{} is not a name...".format(player)

print "Hi {}!".format(player)

money = None
while True:
    print "How much money do you want to bring to a Roulette table?"
    money = raw_input("EUR: ")

    if money.isdigit():
        money = float(money)

        if money > 0:
            print "You play with {:.1f} EUR".format(money)
            break
        else:
            print "{} is not a valid amount...".format(money)
    else:
        print "{} is not a valid amount".format(money)

print """
 *** Please choose your bet type :
(1)Straight
(2)Manque ou Passe
(3)Rouge ou Noir
(4)Pair ou Impair
(5)Dozen Bets
(6)Column Bets

(7)Exit
(8)Help
"""


bet_type = None
func = None
while True:
    if money == 0:
        print "You have no more money to play! See you again!"
        exit()
    bet_type = raw_input("Bet type: ")
    if bet_type.isdigit():
        bet_type = int(bet_type)
        if 1 <= bet_type <= 6:
            func = d[bet_type]
            money = func(money)
        elif bet_type == 7:
            print "Byebye! See You again!"
            exit()
        elif bet_type == 8:
            func = d[bet_type]
            func()
        else:
            print "Invalid bet type!"
    else:
        print "Invalid bet type!"



def checkNumber(input):
    if (str.isdigit()) & (len(input) > 0):
        return True
    else:
        return False
