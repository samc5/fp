import random

def getSum(hand):
    counter = 0
    for i in hand:
        counter += cardValueDict[i]
    return counter
        

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
    
cardValueDict = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}


deckCards = []
for i in cardValueDict.keys():
    for n in range(4):
        deckCards.append(i)
    

def blackjack():
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
    while checkifbust(dealerSum) == False and checkifWin(dealerSum) == False and checkifbust(playerSum) == False and stand == False:
        #Player turn
        print(f'Your Hand: {playerHand}')
        print(f"Dealer's face up card: {dealerHand[0]}")
        dealerSum = getSum(dealerHand)
        playerSum = getSum(playerHand)
        hitStand = input("Hit or stand? Type 'Hit' to hit and anything else to stand")
        if hitStand == "Hit" or hitStand == "hit":
            playerHand.append(deckCards.pop(random.randrange(len(deckCards))))
            print(f'You receive a {playerHand[len(playerHand) - 1]}')
            playerSum = getSum(playerHand)
        else:
            print("You have chosen to Stand")
            #Dealer Turn
            while checkifbust(dealerSum) == False and checkifWin(dealerSum) == False and dealerSum < 17: 
                if dealerSum <= 16:
                    dealerHand.append(deckCards.pop(random.randrange(len(deckCards))))
                    print(f"The dealer receives a {dealerHand[len(dealerHand) - 1]}")
                    dealerSum = getSum(dealerHand)
                #elif dealerSum >= 17:
                    #print("The dealer stands")
                print(f"Dealer's hand: {dealerHand}")
            stand = True
    print(f"Player sum: {playerSum}")
    print(f"Dealer sum: {dealerSum}")
                
    if checkifbust(dealerSum) == True:
        print("The dealer has busted. You win!")
    elif checkifbust(playerSum) == True:
        print("You have busted. The dealer Wins!")
    elif checkifbust(playerSum) == True:
        print("You have blackjack and win!")
    elif checkifWin(dealerSum) == True:
        print("The dealer has blackjack and wins!")
    elif playerSum == dealerSum:
        print("Push!")
    elif playerSum > dealerSum:
        print("You win!")
    elif dealerSum > playerSum:
        print("The dealer wins!")
        

    
    
    
    
blackjack()
    