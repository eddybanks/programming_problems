import math, random
# deque is converts a list into a queue
from collections import deque

# this function removes 7 cards from the deck and gives it to the player
def serve(deck):
  hand = []
  # remove card from deck using popleft function and append it to hand 7 times - range(7) for loop
  for _ in range(7):
    hand.append(deck.popleft())
  
  return hand

# this function represents each round of the game
def play_round(player, player2):
  # if the player is you, print your hand and collection
  if player.turn == 'p':
    player.print()

  # if player doesn't have any cards in hand, check to see if there are cards in the deck to draw from
  if(len(player.hand) == 0):
    # if the deck isn't empty, draw from the deck... else print "You are out of cards"
    if(len(deck) > 0):
      print("Player has no cards in hand and needs to draw")
      player.draw(deck)
    else:
      print("You are out of cards")
      print()
  # if player has cards in hand, ask other opponent for a desired card within the player's hand
  else:
    demand = player.ask()
    # if the card asked for is in the opponent's hand, the oponent loses the card to the player
    if(demand in player2.hand):
      player2.hand.remove(demand)
      if player.turn == 'p':
        print("The computer has a", demand, "and gives it to you")
      else:
        print("You have a", demand, "and give it to the computer")
      # player gains the card and it is added to his hand
      player.add_card(demand)
      print()
      # the player gets to ask again in a repeated round
      play_round(player, player2)
    # if the card asked for is not in the opponent's hand, the player has to draw from the deck
    else:
      print("Go fish!")
      player.draw(deck)
      print()


def calculate(player):
  result = 0
  for i in player.collection:
    result += cards[i]

  if player.turn == 'p':
    print("Your score is", result)
  else:
    print("The computer's score is", result)
  
  return result

class Player:
  def __init__(self, hand, turn):
    self.hand = []
    self.collection = []
    self.turn = turn
    for i in hand:
      self.add_card(i)
    
  def add_card(self, card):
    if card in self.hand:
      self.collection.append(card)
      self.hand.remove(card)
      if self.turn == 'p':
        print("You have a pair of", card)
      else:
        print("The computer has a pair of", card)
    else:
      self.hand.append(card)

  def draw(self, deck):
    drawn = deck.popleft()
    if self.turn == 'p':
      print("You draw a", drawn)
    else:
      print("The computer draws a card")
    
    self.add_card(drawn)

  def ask(self):
    demand = ''
    if self.turn == 'p':
      demand = input("Pick a card to ask for: ")
      if(demand not in self.hand):
        print("Sorry, you don't have any", demand, "in your hand")
        self.ask()
      else:
        print("You ask the computer for a", demand)
    else:
      random.shuffle(self.hand)
      demand = self.hand[0]
      print("The computer asks you for a", demand)
    
    return demand

  def print(self):
    if self.turn == 'p':
      if(len(self.hand) > 0):
        print("Your hand is: ", *self.hand) 
      if(len(self.collection) > 0):
        print("Your collection is: ", *self.collection)
    else:
      if(len(self.hand) > 0):
        print("The computer's hand is", *self.hand)
      if(len(self.collection) > 0):
        print("The computer's collection is: ", *self.collection)


# Program start ----------------------------
# Dictionary of Cards and their values 
cards = {'goldfish': 1, 'catfish': 1, 'trout': 1, 'grouper': 1, 'tuna': 2, 'salmon': 2, 'sturgeon': 2, 'piranha': 3, 'swordfish': 4, 'clownfish': -1 }

# The deck contains 4 of each cards so multiple list of cards by 4
deck = deque([key for key,value in cards.items()] * 4)

# Shuffle deck 
random.shuffle(deck)

player_hand = serve(deck)
computer_hand = serve(deck)
p = Player(player_hand, 'p')
c = Player(computer_hand, 'c')
print()
player = p
player2 = c

while(len(deck) > 0 & (len(player.hand) > 0 | len(player2.hand) > 0)):
  play_round(player, player2)
  # Swap players for the next round
  tmp = player
  player = player2
  player2 = tmp


p.print()
p1 = calculate(p)
c.print()
p2 = calculate(c)
if(p1 > p2):
  winner ="you"
else:
  winner = "the computer"
print("The winner is ", winner)