# -*- coding: utf-8 -*-
import random
from sys import exit



def straight(input):
    print "You play straight! Enter your bets: "

    while True:
        amount = raw_input("I play Euro: ")
        if amount.isdigit():
            amount = float(amount)
            if (input - amount >= 0) & (amount >= 0):
                bet = int(raw_input("{} Euro on: ".format(amount)))
                if 0 <= bet <= 36:
                    print "{} Euro on {}. No more bets please!".format(amount, bet)
                    rnd = random.randint(0,36)
                    if rnd in red:
                        print "{} Red".format(rnd)
                    if rnd in black:
                        print "{} Black".format(rnd)

                    if rnd == bet:
                        print "You Win {} Euro".format(amount*35)
                        input += amount * 35
                        print "New bank acount: {} Euro".format(input)
                        break
                    else:
                        print "You Lose {} Euro".format(amount)
                        input -= amount
                        print "New bank account: {} Euro".format(input)
                        break
                else:
                    print "invalid bet... try again!"
                    continue

        else:
            print "invalid bet..."

    return input

def manque(input):
    print "manque"
    return

def passe(input):
    print "passe"
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

def helpme(*args):
    print """
    *** Roulette Guide ***
    (1) Straight (or Single) a bet on a single number [35 to 1]
    (2) 1 to 18 (Manque) a bet on one of the rst 18 numbers. [1 to 1]
    (3) 19 to 36 (Passe) a bet on the high 18 numbers. [1 to 1]
    (4) Red or Black (Rouge ou Noir) a bet on which color the roulette wheel will show. [1 to 1]
    (5) Even or odd (Pair ou Impair) a bet on even or odd nonzero number. [1 to 1]
    (6) Dozen Bets a bet on the rst 12 (1-12), second 12 (13-24) or third 12 (25-36) numbers. [2 to 1]
    (7) Column Bets a bet on one of the three vertical lines e.g.: 1-4-7-10 . . . [2 to 1]

    The numbers in [] represent the payout of each bet e.g. [2 to 1] means that you get 2 times
    the amount you bet from the bank. Good Luck!
    """
    return

d = {1 : straight, 2 : manque, 3 : passe, 4 : rouge_ou_noir, 5 : pair_ou_impair, 6 : dozen_bets, 7 : column_bets, 9 : helpme}
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = 0

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
    money = raw_input("Euro: ")

    if money.isdigit():
        money = float(money)

        if money > 0:
            print "You play with {:.2f} Euro".format(money)
            break
        else:
            print "{} is not a valid amount...".format(money)
    else:
        print "{} is not a valid amount".format(money)

print """
 *** Please choose your bet type :
(1)Straight
(2)Manque
(3)Passe
(4)Rouge ou Noir
(5)Pair ou Impair
(6)Dozen Bets
(7)Column Bets

(8)Exit
(9)Help
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
        if 1 <= bet_type <= 7:
            func = d[bet_type]
            money = func(money)
        elif bet_type == 8:
            print "Byebye!"
            exit()
        elif bet_type == 9:
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
