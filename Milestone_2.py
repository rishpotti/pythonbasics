import random
suits = ("Hearts", "Spades", "Clubs", "Diamonds")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

class Card:
    
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    

class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                 new_card = Card(rank, suit)
                 
                 self.all_cards.append(new_card)
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+ Card.__str__()
        return 'The deck has:' + deck_comp
            
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
class Player():
    
    def __init__(self, account):
        
        self.account = account
        self.hand = []
        self.value = 0
        self.aces = 0
        self.bet = 0
    
    def add_card(self, new_card):
        self.hand.append(new_card)
        self.value += values[new_card.rank]
        if new_card.rank == "Ace":
            self.aces += 1
        
        
    def ace_adjust(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
            
    def win_bet(self):
        self.account += self.bet
    
    def lose_bet(self):
        self.account -= self.bet
    
    def __str__(self):
        return f'Player balance is {self.account}'
    
def take_bet():
    while True:
        try:
            Player.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if Player.bet > Player.account:
                print("Sorry, your bet can't exceed", Player.account)
            else:
                break
        
def hit(Deck, Player):
    
    Player.add_card(Deck.deal())
    Player.ace_adjust()
    
def hit_or_stand(Deck, Player):
    playing = True
    
    while playing:
        x = int(input('Enter 1 to hit and 0 to stand:'))
        if x == 1:
            hit(Deck, Player)
         
        elif x == 0:
            print("Player stands. Dealer plays.")
            playing = False
        
        else:
            print("Error. Please try again.")
            continue
            
        break

def show_some(player1, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player1.cards, sep='\n ')
    
def show_all(player1,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player1.cards, sep='\n ')
    print("Player's Hand =",player1.value)
    
def player_busts(player1,dealer,Player):
    print("Player busts!")
    Player.lose_bet()

def player_wins(player1,dealer,Player):
    print("Player wins!")
    Player.win_bet()

def dealer_busts(player1,dealer,Player):
    print("Dealer busts!")
    Player.win_bet()
    
def dealer_wins(player1,dealer,Player):
    print("Dealer wins!")
    Player.lose_bet()
    
def push(player1,dealer):
    print("Dealer and Player tie! It's a push.")
    
play = True

while True:
    print('Welcome to python Blackjack! Try and get as close to 21 as possible \nwithout going over.')
    
    