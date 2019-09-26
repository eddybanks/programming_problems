import math, random
from collections import deque

def serve(deck):
  hand = []
  for _ in range(7):
    hand.append(deck.popleft())
  
  return hand

class Player:
  def __init__(self, hand):
    self.hand = {x:hand.count(x) for x in hand}
    self.collection = {}
    self.check_collection()
    self.player = "You"

  def check_collection(self):
    for k,v in self.hand.items():
      if(v >= 2):
        count = math.floor(v/2)
        self.collection[k] = count
        for _ in range(count):
          self.hand[k] -= count * 2
    
    for k,v in self.collection.items():
      print("You have a pair of", k)


  def draw(self, deck):
    drawn = deck.popleft()
    if drawn in self.hand:
      self.hand[drawn] += 1
      self.check_collection()
    else:
      self.hand[drawn] = 1

  def show_cards(self):
    hand = []
    collection = []
    for k,v in self.hand.items():
      if(v == 1):
        hand.append(k)
    
    for k,v in self.collection.items():
      for _ in range(v):
        collection.append(k)

    print("Your hand is: ")
    print("Your collection is: ")

# Dictionary of Cards and their values 
cards = {'goldfish': 1, 'catfish': 1, 'trout': 1, 'grouper': 1, 'tuna': 2, 'salmon': 2, 'sturgeon': 2, 'piranha': 3, 'swordfish': 4, 'clownfish': -1 }

# The deck contains 4 of each cards so multiple list of cards by 4
deck = deque([key for key,value in cards.items()] * 4)

# Shuffle deck 
random.shuffle(deck)
print('-----------Deck----------------')
print(deck)
player_hand = serve(deck)
computer_hand = serve(deck)
p = Player(player_hand)
print(p.hand)
print(p.collection)

p.draw(deck)
print(p.hand)
print(p.collection)
print(deck)
