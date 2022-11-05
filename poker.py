"""
Poker Game using functions, lists, and tuples
Name: Sufyan
"""
import random
#first have to make the deck
deck = [("Ace","Spades"),("King","Spades"),("Queen","Spades"),("Jack","Spades"),("Ten","Spades"),("Nine","Spades"),("Eight","Spades"),("Seven","Spades"),("Six","Spades"),("Five","Spades"),("Four","Spades"),("Three","Spades"),("Two","Spades"),
        ("Ace","Clovers"),("King","Clovers"),("Queen","Clovers"),("Jack","Clovers"),("Ten","Clovers"),("Nine","Clovers"),("Eight","Clovers"),("Seven","Clovers"),("Six","Clovers"),("Five","Clovers"),("Four","Clovers"),("Three","Clovers"),("Two","Clovers"),
        ("Ace","Hearts"),("King","Hearts"),("Queen","Hearts"),("Jack","Hearts"),("Ten","Hearts"),("Nine","Hearts"),("Eight","Hearts"),("Seven","Hearts"),("Six","Hearts"),("Five","Hearts"),("Four","Hearts"),("Three","Hearts"),("Two","Hearts"),
        ("Ace","Diamonds"),("King","Diamonds"),("Queen","Diamonds"),("Jack","Diamonds"),("Ten","Diamonds"),("Nine","Diamonds"),("Eight","Diamonds"),("Seven","Diamonds"),("Six","Diamonds"),("Five","Diamonds"),("Four","Diamonds"),("Three","Diamonds"),("Two","Diamonds")]
random.shuffle(deck)


check = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
high = 0
num = []
i = 0
def checkhighcard(hand):
    check = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
    high = 0
    num = []
    i = 0
    hcard = []
    for items in hand:
        items = hand[i][0]
        num += items.split()
        i = i + 1

    for cards in num:
        for x in check:
            if cards == x:
                index = check.index(x)
                hcard.append(index)
    hcard.sort
    del hcard[1:5]
    hcard = check[hcard[0]]
    return hcard

def checkstraight(hand):
    check = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
    high = 0
    num = []
    i = 0
    straight=[]
    for items in hand:
        items = hand[i][0]
        num += items.split()
        i = i + 1
    for cards in num:
        for x in check:
            if cards == x:
                index = check.index(x)
                straight.append(index)
    straight.sort()
    s = 0
    if straight[4]-straight[3] == 1 and straight[3]-straight[2] == 1 and straight[2]-straight[1] == 1 and straight[1]-straight[0] == 1:
        straight = True
        return True
def checkroyal(hand):
    check = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
    high = 0
    num = []
    i = 0
    straight=[]
    for items in hand:
        items = hand[i][0]
        num += items.split()
        i = i + 1
    for cards in num:
        for x in check:
            if cards == x:
                index = check.index(x)
                straight.append(index)
    straight.sort()
    royal=" "
    if straight[0] == 0 and straight[1] == 1 and straight[2] == 2 and straight[3] == 3 and straight[4] == 4:
        royal = True
        return True
    
def checkonepair(hand):
    check = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
    high = 0
    num = []
    i = 0
    for items in hand:
        items = hand[i][0]
        num += items.split()
        i = i + 1
                
    for cards in num:
        pair = num.count(cards)
        if pair == 2:
            onepair = True
            num.remove(cards)
            return True
def checktwopair(hand):
    check = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
    high = 0
    num = []
    i = 0
    twopair = 0
    for items in hand:
        items = hand[i][0]
        num += items.split()
        i = i + 1
        
    for cards in num:
        pair = num.count(cards)
        if pair == 2:
            num.remove(cards)
            twopair = twopair + 1
            high = high + 1
            if twopair== 2:
                return True
                break

def checkthreeofakind(hand):
    check = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
    high = 0
    num = []
    i = 0
    for items in hand:
        items = hand[i][0]
        num += items.split()
        i = i + 1
       
    for cards in num:
        pair = num.count(cards)
        if pair ==3:
            return True
            num.remove(cards)
            num.remove(cards)
            high = high + 1

def checkfourofakind(hand):
    check = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
    high = 0
    num = []
    i = 0
    for items in hand:
        items = hand[i][0]
        num += items.split()
        i = i + 1
                
    for cards in num:
        pair = num.count(cards)
        if pair ==4:
            fourkind = True
            num.remove(cards)
            num.remove(cards)
            num.remove(cards)
            high = high + 1
            return True

def checkflush(hand):
    check = ["Ace","King","Queen","Jack","Ten","Nine","Eight","Seven","Six","Five","Four","Three","Two"]
    high = 0
    num = []
    i = 0
    for items in hand:
        items = hand[i][0]
        num += items.split()
        i = i + 1
    
    suit = []
    i = 0
    for items in hand:
        items = hand[i][1]
        suit +=items.split()
        i = i + 1
    for cards in suit:
        flush = suit.count(cards)
        if flush == 5:
            flush = True
            high = high + 1
            return True
            break
playerOne = (random.sample(deck,5))
for i in playerOne:
    deck.remove(i)
playerTwo = (random.sample(deck,5))

checkhighcard(playerOne)
checkhighcard(playerTwo)

checkstraight(playerOne)
checkstraight(playerTwo)

checkflush(playerOne)
checkflush(playerTwo)

checkonepair(playerOne)
checkonepair(playerTwo)

checktwopair(playerOne)
checktwopair(playerTwo)

checkthreeofakind(playerOne)
checkthreeofakind(playerTwo)

checkfourofakind(playerOne)
checkfourofakind(playerTwo)

checkroyal(playerOne)
checkroyal(playerTwo)

rankone = 0

if checkroyal(playerOne) == True and checkflush(playerOne) == True and checkstraight(playerOne) == True:
    rankone = 10

elif checkstraight(playerOne) == True and checkflush(playerOne) == True:
    rankone = 9
    
elif checkfourofakind(playerOne) == True:
    rankone = 8
    
elif checkonepair(playerOne) == True and checkthreeofakind(playerOne) == True:
    rankone = 7
    
elif checkflush(playerOne) == True:
    rankone = 6
elif checkstraight(playerOne) == True:
    rankone = 5
elif checkthreeofakind(playerOne) == True:
    rankone = 4
elif checktwopair(playerOne) == True:
    rankone = 3
elif checkonepair(playerOne) == True:
    rankone = 2
else:
    rankone = 1

ranktwo = 0
if checkroyal(playerTwo) == True and checkflush(playerTwo) == True and checkstraight(playerTwo) == True:
    ranktwo = 10

elif checkstraight(playerTwo) == True and checkflush(playerTwo) == True:
    ranktwo = 9
    
elif checkfourofakind(playerOne) == True:
    ranktwo = 8
    
elif checkonepair(playerTwo) == True and checkthreeofakind(playerTwo) == True:
    ranktwo = 7
    
elif checkflush(playerTwo) == True:
    ranktwo = 6
    
elif checkstraight(playerTwo) == True:
    ranktwo = 5
    
elif checkthreeofakind(playerTwo) == True:
    ranktwo = 4
    
elif checktwopair(playerTwo) == True:
    ranktwo = 3
    
elif checkonepair(playerTwo) == True:
    ranktwo = 2
    
else:
    ranktwo = 1

print(playerOne)
print("\n",playerTwo)
#general better hand
if rankone > ranktwo:
    print("Player One wins.")
elif ranktwo > rankone:
    print("Player Two wins.")
#stronger straights
elif rankone == 9 and ranktwo == 9:
    if checkhighcard(playerOne) > checkhighcard(playerTwo):
        print("Player One wins.")
    elif checkhighcard(playerOne) < checkhighcard(playerTwo):
        print("Player two wins.")
    else:
        print("Its a draw!")

elif rankone == 5 and ranktwo == 5:
    if checkhighcard(playerOne) > checkhighcard(playerTwo):
        print("Player One wins.")
    elif checkhighcard(playerOne) < checkhighcard(playerTwo):
        print("Player two wins.")
    else:
        print("Its a draw!")

elif ranktwo == rankone:
    print("Its a draw!")
elif checkhighcard(playerOne) > checkhighcard(playerTwo):
    print("Player 1 wins.")
elif checkhighcard(playerOne) < checkhighcard(playerTwo):
    print("Player two wins.")
else:
    print("Its a draw!")

