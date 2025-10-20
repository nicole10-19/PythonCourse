#Inheritance 
import random

class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank= rank

        #suits and ranks are class variables 
        #suits and rank are instance attributes 
    def __eq__(self, other):
        return( self.suit == other.suit   and self.rank== other.rank)
    
    def to_tuple(self):
        return(self.suit, self.rank)
    
    def __lt__(self, other):
        #Suits is more important than rank 
        #If suits are equal, compare ranks 
        return self.to_tuple() < other.to_tuple()
    
    def __le__(self ,other):
        return self.to_tuple() <= other.to_tuple
    

class Deck:
    def __init__(self, cards):
        self.cards=cards
    
    def __str(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def make_cards():
        cards=[]
        for suit in range(4):
            #Aces outrank kings 
            for rank in range (2,15):
                card = Card(suit,rank)
                cards.append(card)
        return cards
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort
    
    def take_card(self):
        return self.cards.pop()

    def put_card(self, card):
        self.cards.apppenf(card)

    def move_cards(self, other, num):
        for _ in range(num):
            card = self.take_card
            other.put_card(card)

#Parens and children 

class Hand(Deck):

    def __init__(self, label=''):
        self.label= label
        self.cards = []

cards = Deck.make_cards()
deck = Deck(cards)


for card in deck.cards[:3]:
    print(card)
queen = Card(1,12)

print(queen.suits)
