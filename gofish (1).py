import random

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    
    def __str__(self):
        return self.rank + " of " +self.suit

class Deck:
    def __init__(self):
        self.deck = []
        self.makeDeck()

    def makeDeck(self):
        suits = ["diamonds","hearts","spades","clubs"] 
        ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def numCards(self):
        return len(self.deck)
        
    def __str__(self):
        answer = ""
        for card in self.deck:
            answer += str(card) + "\n"
        return answer + ""
    
    def deal(self):
        i = random.randint(0,len(self.deck)-1)
        return self.deck.pop(i)
    
class GoFish:
    def __init__(self):
        self.correctguess = False
        self.hand1 = []
        self.hand2 = []
        self.score1 = 0
        self.score2 = 0
        self.deck = Deck()
        self.inhand = False
        self.ownhand = False
        for i in range(7):
            self.hand1.append(self.deck.deal())
        for i in range(7):
            self.hand2.append(self.deck.deal())

    def CheckSet(self,hand):
        ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        z=0
        i=0
        for r in range(len(ranks)):
            z=0
            for card in hand:
                if ranks[r]== card.getRank():
                    z+=1
                
            if z == 4:
                for p in range (len(hand)-1,-1,-1):
                    if hand[p].getRank() == ranks[r]:
                        hand.pop(p)
                if hand == self.hand1:
                    self.score1+=1
                else:
                    self.score2+=1

    def getScore1(self):
        return self.score1
    
    def getScore2(self):
        return self.score2
    
    def getHandOne(self):
        return self.hand1
    
    def getHandTwo(self):
        return self.hand2
    
    def askCard(self,ask,turn):
        self.inhand = False
        self.ownhand = False
        if str(ask).isdigit() == False:
            ask = ask.capitalize()
        
        if turn%2 == 0:
            for i in range (len(self.hand1)-1,-1,-1):
                if self.hand1[i].getRank().find(ask)>=0:
                    self.ownhand = True

            if self.ownhand == True:
                for i in range (len(self.hand2)-1,-1,-1):
                    if self.hand2[i].getRank() == ask:
                        self.hand1.append(self.hand2[i])
                        self.hand2.pop(i)
                        self.inhand = True
            
        else:
            for i in range (len(self.hand2)-1,-1,-1):
                if self.hand2[i].getRank().find(ask)>=0:
                    self.ownhand = True

            if self.ownhand == True:
                for i in range (len(self.hand1)-1,-1,-1):
                    if self.hand1[i].getRank() == ask:
                        self.hand2.append(self.hand1[i])
                        self.hand1.pop(i)
                        self.inhand = True
                
    def fishCard(self,hand,ask):
        if str(ask).isdigit() == False:
            ask = ask.capitalize()
        if self.inhand == False:
            hand.append(self.deck.deal())
            if hand[len(hand)-1].getRank()==ask:
                self.correctguess = True
            else:
                self.correctguess = False
        
    
    
    def getCardsLeft(self):
        return self.deck.numCards()

    def getcorrectGuess(self):
        return self.correctguess
    
    def ownHand(self):
        return self.ownhand

    def inHand(self):
        return self.inhand
                
    


game = GoFish()
turn = 0

while game.getCardsLeft() >0:
    hOne =', '.join([str(card.getRank()) for card in game.getHandOne()])
    hTwo =', '.join(["?" for card in game.getHandTwo()])
    print ("POne hand is: " + hOne)
    print ("POne score is: " + str(game.getScore1()))
    print ("")
    print ("PTwo hand is: " + hTwo)
    print ("PTwo score is: " + str(game.getScore2()))
    print ("")
    print (str(game.getCardsLeft()) + " cards remaining in deck")
    if turn%2 == 0 :
        print ("")
        ask = input("pick a card to fish for:  ")
        if len(game.getHandTwo())<0:
            game.fishCard(game.getHandOne(),ask)
        game.askCard(ask,turn)
        game.CheckSet(game.getHandOne())
        if game.ownHand() == False:
            print("")
            print("YOU CAN ONLY ASK FOR A CARD IN YOUR OWN DECK!! try again!")
            print("")
        else:
            if game.inHand()==True:
                print("")
                print (ask+ " was in the computers deck! go again!")
                print("")
            else:
                game.fishCard(game.getHandOne(),ask)
                print (ask + " was not in the computers deck. go fish")
                print("")

                if game.getcorrectGuess()==True:
                    print("you fished your wish of a " +ask+ "! go again!")
                    game.CheckSet(game.getHandOne())

                else:
                    print("you did not fish your wish: you got a  " + str(game.getHandOne()[len(game.getHandOne())-1].getRank()))
                    print("")
                    turn+=1
                    game.CheckSet(game.getHandOne())

            
        
    

    else:
        print ("")
        input("please select a key for computer to take turn: ")
        if len(game.getHandTwo())>0:
            c = random.randint(0,len(game.getHandTwo())-1)
        else:
            game.fishCard(game.getHandTwo(),c)
        ask = game.getHandTwo()[c].getRank()
        game.askCard(ask,turn)
        game.CheckSet(game.getHandTwo())
        print ("computer selected " +str(ask))
        if game.inHand()==True:
            print (ask+ " was in your deck! computer goes again!")
            print("")
        else:
            game.fishCard(game.getHandTwo(),ask)
            print (ask + " was not in your deck. computer go fish")
            print("")
            if game.getcorrectGuess()==True:

                print("computer fished their wish of a " +ask+ "! computer goes again!")
                game.CheckSet(game.getHandTwo())
            else:
               
                print("computer did not fish their wish: fished a " + str(game.getHandTwo()[len(game.getHandTwo())-1].getRank()))
                print("")
                turn+=1
                game.CheckSet(game.getHandTwo())
            
if game.getScore1()>game.getScore2():
    print("thanks for playing! you had more points you won!!")
else:
    print("thanks for playing! the computer had more points you lost. better luck next time!")
    

