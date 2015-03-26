# -*- coding: utf-8 -*-
import random
from sys import exit

d = {1 : "Straight", 2 : "Manque", 3 : "Passe", 4 : "Rouge ou Noir", 5 : "Pair ou Impair" , 6 : "Dozen Bets", 7 : "Column Bets"}
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = 0

print "** Welcome to Group 7 Roulette **"

print "Enter your name :"
player = raw_input("> ")

print "Hi %s, how much money do you want to bring to a Roulette table?" % player

money = float(raw_input("> € "))

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
"""
bet_type = int(raw_input("> "))

for i in d:
    if bet_type == i:
        print "Good ! {} ".format(d[i])
    else:
        exit()
