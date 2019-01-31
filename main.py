import pandas as pd
import numpy as np
import random as ran

## Get Hand Totals
def handTot(hand):
    sum = 0
    for i in hand:
        sum = sum + i
    return sum

## Play Game
def play(player):
    bet = input("Please place a bet.")
    while (int(bet) > player and int(bet) < 0):
        bet = input("You do not have enough money, please place another bet.")
    bet = int(bet)

    dealer = [ran.randint(1, 11), ran.randint(1, 11)]
    hand = [ran.randint(1, 11), ran.randint(1, 11)]
    print("Dealers Visible Card:")
    print(dealer[1])
    print("Your Cards:")
    str = "[{}, {}] = {}"
    print(str.format(hand[0], hand[1], handTot(hand)))
    notBusted = True
    while (notBusted):
        sum = handTot(hand)
        if (sum < 21):
            print("Would you like to:")
            print("1: Hit")
            print("2: Stand")
            print("3: See Dealers Hand")
            choice = input()
            choice = int(choice)
            if (choice == 1):
                card = ran.randint(1, 11)
                hand.append(card)
                str = "Your hand: {} = {}"
                print(str.format(hand, handTot(hand)))
                print()
            elif (choice == 3):
                str = "The Dealers Hand: {}"
                print(str.format(dealer))
            else:
                notBusted = False
        else:
            notBusted = False
    while (handTot(dealer) < 16):
        dealer.append(ran.randint(1, 11))

    str = "Your hand is {} = {}, The dealer had {} = {} "
    print(str.format(hand, handTot(hand), dealer, handTot(dealer)))
    if (handTot(hand) > handTot(dealer) and handTot(hand) < 22 and handTot(dealer) < 22):
        str = "You won {}"
        print(str.format(bet))
        player = player + bet
    elif (handTot(dealer) > 21 or handTot(dealer) == handTot(hand)):
        str = "You tied and get your money back"
        print(str)
    else:
        str = "You lost {}"
        print(str.format(bet))
        player = player - bet
    return player

player = 100
game = True

## Start the program
while(game):
    print("What would you like to do:")
    print("1: Play a game")
    print("2: Check your balance")
    print("3: Quit")
    choice = input()
    choice = int(choice)
    if(choice == 3):
        game = False
    elif(choice == 2):
        str = "Your balance is: {}"
        print(str.format(player))
        print()
    else:
        player = play(player)
        print()