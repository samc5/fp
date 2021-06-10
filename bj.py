import random

def getSum(hand):
    counter = 0
    for i in hand:
        counter += cardValueDict[i]
    return counter
        
def textToBool(text):
    if text == "y" or text == "Y" or text == "Yes" or text == "yes":
        return True
    else:
        return False

def checkifbust(total):
    if total > 21:
        return True
    else:
        return False
    
def checkifWin(total):
    if total == 21:
        return True
    else:
        return False
    
def checkValidBet(bet, money):
    if bet > money or bet < 0 or bet != int(bet):
        print("Nice try. Enter a real bet - a positive integer that you can afford")
        bet = checkValidBet(int(input("How much do you want to bet?")), money) 
    return bet
    
cardValueDict = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}


deckCards = []
for i in cardValueDict.keys():
    for n in range(4):
        deckCards.append(i)
    

def blackjack():
    currentMoney = 1000
    x = True
    while x != False:
        print(f'You have {currentMoney}')
        bet = checkValidBet(int(input("How much do you want to bet?")), currentMoney)    
        stand = False
        #MAKING THE DECK
        deckCards = []
        for i in cardValueDict.keys():
            for n in range(4):
                deckCards.append(i)
        #DEALING THE HANDS
        dealerHand = [] 
        playerHand = []
        dealerSum = 0
        playerSum = 0
        playerHand.append(deckCards.pop(random.randrange(len(deckCards))))
        dealerHand.append(deckCards.pop(random.randrange(len(deckCards))))
        playerHand.append(deckCards.pop(random.randrange(len(deckCards))))
        dealerHand.append(deckCards.pop(random.randrange(len(deckCards))))
        playerSum = getSum(playerHand)
        dealerSum = getSum(dealerHand)
        if playerSum == 21:
            print("You have blackjack and win!")
            x = textToBool(input("Would you like to play again? Y or N"))
            currentMoney += (bet * 1.5)
        while checkifbust(dealerSum) == False and checkifWin(dealerSum) == False and checkifbust(playerSum) == False and stand == False:
            #Player turn
            if playerSum == 21:
                print("You have blackjack and win!")
                x = textToBool(input("Would you like to play again? Y or N"))
                currentMoney += (bet * 1.5)
            print(f'Your Hand: {playerHand}')
            print(f"Dealer's face up card: {dealerHand[0]}")
            dealerSum = getSum(dealerHand)
            playerSum = getSum(playerHand)
            hitStand = input("Hit or stand? Type 'Hit' to hit and anything else to stand")
            if playerSum == 21:
                    print("You have blackjack and win!")
                    x = textToBool(input("Would you like to play again? Y or N"))
                    currentMoney += (bet * 1.5)
                
            if hitStand == "Hit" or hitStand == "hit":
                playerHand.append(deckCards.pop(random.randrange(len(deckCards))))
                print(f'You receive a {playerHand[len(playerHand) - 1]}')
                playerSum = getSum(playerHand)
                if playerSum > 21:
                    if 'Ace' in playerHand:
                        playerSum -= 10
                
            else:
                print("You have chosen to Stand")
                #Dealer Turn
                while checkifbust(dealerSum) == False and checkifWin(dealerSum) == False and dealerSum < 17: 
                    if dealerSum <= 16:
                        dealerHand.append(deckCards.pop(random.randrange(len(deckCards))))
                        print(f"The dealer receives a {dealerHand[len(dealerHand) - 1]}")
                        dealerSum = getSum(dealerHand)
                    print(f"Dealer's hand: {dealerHand}")
                    if dealerSum > 21:
                        if 'Ace' in dealerHand:
                            dealerSum -= 10
                stand = True
                if playerSum > 21:
                    if 'Ace' in playerHand:
                        playerSum -= 10
        print(f"Player sum: {playerSum}")
        print(f"Dealer sum: {dealerSum}")
        
        if checkifbust(dealerSum) == True:
            print("The dealer has busted. You win!")
            x = textToBool(input("Would you like to play again? Y or N"))
            currentMoney += bet
        elif checkifbust(playerSum) == True:
            print("You have busted. The dealer Wins!")
            x = textToBool(input("Would you like to play again? Y or N"))
            currentMoney -= bet
        elif checkifbust(playerSum) == True:
            print("You have blackjack and win!")
            x = textToBool(input("Would you like to play again? Y or N"))
            currentMoney += bet
        elif checkifWin(dealerSum) == True:
            print("The dealer has blackjack and wins!")
            x = textToBool(input("Would you like to play again? Y or N"))
            currentMoney -= bet
        elif playerSum == dealerSum:
            print("Push!")
            x = textToBool(input("Would you like to play again? Y or N"))
        elif playerSum > dealerSum:
            print("You win!")
            x = textToBool(input("Would you like to play again? Y or N"))
            currentMoney += bet
        elif dealerSum > playerSum:
            print("The dealer wins!")
            x = textToBool(input("Would you like to play again? Y or N"))
            currentMoney -= bet
        

    
    
    
    
blackjack()
    