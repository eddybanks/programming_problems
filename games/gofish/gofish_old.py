import math, random
from collections import deque

def serve(deck):
  hand = []
  for _ in range(7):
    hand.append(deck.popleft())
  
  return hand


class Player:
  def __init__(self, hand, turn):
    self.hand = []
    self.collection = []
    self.turn = turn
    self.dictionary = {x:hand.count(x) for x in hand}
    self.check_collection()

  def check_collection(self):
    # for k,v in self.hand.items():
    #   if(v >= 2):
    #     count = math.floor(v/2)
    #     self.collection[k] = count
    #     for _ in range(count):
    #       self.hand[k] -= count * 2
    
    # for k,v in self.collection.items():
    #   if(self.turn == 'p'):
    #     print("You have a pair of", k)
    #   else:
    #     print("The computer has a pair of", k)

    if(self.turn == 'p'):
      print("You have a pair of", k)
    else:
      print("The computer has a pair of", k)

  def draw(self, deck):
    drawn = deck.popleft()
    if self.turn == 'p':
      print("You draw a", drawn)
    else:
      print("The computer draws a card")

    if drawn in self.hand:
      # self.hand[drawn] += 1
      # self.check_collection()
      self.collection.append(drawn)
    else:
      # self.hand[drawn] = 1
      self.hand.append(drawn)

  def ask(self):
    demand = ''
    if self.turn == 'p':
      demand = input("Pick a card to ask for: ")
      print("You ask the computer for a", demand)
    else:
      # hand = list(self.hand)
      random.shuffle(self.hand)
      demand = self.hand[0]
      print("The computer asks you for a", demand)
    
    return demand

  def print(self):
    # hand = []
    # collection = []
    # for k,v in self.hand.items():
    #   if(v == 1):
    #     hand.append(k)
    
    # for k,v in self.collection.items():
    #   for _ in range(v):
    #     collection.append(k)

    print("Your hand is: ", *self.hand)
    print("Your collection is: ", *self.collection)

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

# while(len(deck) > 0):
p.print()
demand = p.ask()
if(demand in c.hand | demand in c.collection):


