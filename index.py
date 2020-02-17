import random
# Dealer cards
dealerCards = []
# Player cards
playerCards = []


def addCard(hand):
    hand.append(random.randint(1, 11))


def convertListToString(list):
    return ''.join(str(e) + ", " for e in list)[:-2]


while len(dealerCards) != 2:
    addCard(dealerCards)
    if len(dealerCards) == 2:
        print("Dealer has: X,", dealerCards[1])

while len(playerCards) != 2:
    addCard(playerCards)
    if len(playerCards) == 2:
        print("You have:", convertListToString(playerCards))

if sum(dealerCards) == 21:
    print("Dealer has 21 and wins!")
    exit()

elif sum(dealerCards) > 21:
    print("Dealer has busted!")

while sum(playerCards) < 21:
    actionTaken = str(input("Do you want to stay or hit? "))
    if actionTaken == "hit":
        addCard(playerCards)
        print("You now have a total of " + str(sum(playerCards)) +
              " from these cards:", playerCards)
    else:
        print("The dealer has a total of " +
              str(sum(dealerCards)) + " with:", dealerCards)
        print("You have a total of " +
              str(sum(playerCards)) + " with:", playerCards)
        if sum(dealerCards) > sum(playerCards):
            print("Dealer wins!")
        else:
            print("You win!")
            break
    print("===============================")

if sum(playerCards) > 21:
    print("You busted! Dealer wins.")
elif sum(playerCards) == 21:
    print("You got a blackjack! You win!!!")
