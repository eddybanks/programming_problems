gofish.py
Write a program that plays the card game Go Fish with the user. Here are the rules of the game, along with some implementation notes:

Our version of Go Fish is for 2 players: one human and one AI. The human always plays first.
Our version of Go Fish is played with a deck of 40 cards. There are 4 each of goldfish, catfish, trout, grouper, tuna, salmon, sturgeon, piranha, swordfish, and clownfish. You can represent each card as a string with the appropriate name, e.g. 'goldfish'.
The deck is shuffled into a random order before play begins.
Each player is dealt an initial hand of 7 cards at random. The remaining cards form the draw pile.
If at any time (including at the start of the game) a player has two matching cards in their hand (e.g., two sturgeon), they form a pair. The player immediately discards the pair from their hand and puts the pair in their collection.
On their turn, a player asks another player of their choice, “Do you have any [blank]?” and names a fish from their own hand. Your program should prompt the player to choose a card to ask for. On its turn, the AI should choose a card to ask for at random.
If the player being asked has one of the requested cards in their hand, they give it to the asking player (who now has a pair and should discard and score it). The asking player takes another turn.
If the player being asked does not have the requested card in their hand, they say “Go fish!” The asking player draws the top card from the draw pile. Even if it forms a pair, they do not take another turn.
Each pair of cards has a value which represents the number of points it is worth. The values are:
goldfish: 1
catfish: 1
trout: 1
grouper: 1
tuna: 2
salmon: 2
sturgeon: 2
piranha: 3
swordfish: 4
clownfish: -1
A player’s score is the total of the values of the cards in their collection.
The game ends when either (a) one player is out of cards, or (b) the draw pile is out of cards. Any remaining pairs in players’ hands are placed in their collections. The player with the highest score wins.
There is a sample transcript of the program’s output in transcript.txt. Note that the bulk of your grade will be based on correctly implementing the rules of Go Fish; focus on formatting the output correctly only once you have the gameplay code working. (That said, if you have persistent difficulty getting an output to match, it may be an indication that there is something off about your program’s logic.)

Hints: Do functions.py first. You will need to use the random module, as in the Fill-in-the-Blanks program from Lab 2. The demonstration program in Lab 3 will be a simpler interactive game, so you may find that helpful as a starting point.