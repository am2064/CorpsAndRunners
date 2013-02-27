#!/usr/bin/python
import random

deck=[
"Nisei MK II Agenda",
"Nisei MK II Agenda",
"Nisei MK II Agenda",
"Project Junebug Asset",
"Project Junebug Asset",
"Project Junebug Asset",
"Snare! Asset",
"Snare! Asset",
"Snare! Asset",
"Zaibatsu Loyalty Asset",
"Cell Portal Ice",
"Cell Portal Ice",
"Chum Ice",
"Chum Ice",
"Data Mine Ice",
"Data Mine Ice",
"Neural Katana Ice",
"Neural Katana Ice",
"Neural Katana Ice",
"Wall of Thorns Ice",
"Wall of Thorns Ice",
"Wall of Thorns Ice",
"Jinteki Identity",
"Neural EMP Operation",
"Neural EMP Operation",
"Precognition Operation",
"Precognition Operation",
"Akitaro Watanabe Upgrade",
"Priority Requisition Agenda",
"Priority Requisition Agenda",
"Priority Requisition Agenda",
"Private Security Force Agenda",
"Private Security Force Agenda",
"Private Security Force Agenda",
"Melange Mining Corp. Asset",
"Melange Mining Corp. Asset",
"Enigma Ice",
"Enigma Ice",
"Enigma Ice",
"Hunter Ice",
"Hunter Ice",
"Wall of Static Ice",
"Wall of Static Ice",
"Wall of Static Ice",
"Hedge Fund Operation",
"Hedge Fund Operation",
"Hedge Fund Operation",
"PAD Campaign Upgrade",
"PAD Campaign Upgrade",
"PAD Campaign Upgrade"
]

random.shuffle(deck)

hand=[deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop()]
archives = []
server = ["Archives", "R+D", "HQ"]
advances = [0,0,0]
upgrades = []

clicks = 3

hand.append(deck.pop())

while(deck):
	while(clicks > 0 ):
		print("Hand: ")
		print(hand)
		print("Field: ")
		print(server)
		print(advances)
		print(upgrades)
		print("1. Draw - 1 Click")
		print("2. Play - 1 Click and oddities")
		print("3. Advance - 1 Click, 1 Credit")
		print("4. Place in Archives - Free")
		print("5. View R+D - Free")
		print("6. View Archives - Free")
		print("Clicks left: " + str(clicks))
		selection = raw_input()
		if(selection is "1"):
			hand.append(deck.pop())
			clicks = clicks - 1
		elif(selection is "2"):
			print("1. Remote Server")
			print("2. Ice")
			print("3. Operation")
			print("4. Upgrade")
			selection = raw_input()
			if( selection is "1" ) :
				print(hand)
				print("Card? (0-index, left to right)")
				selection = raw_input()
				server.append(hand.pop(int(selection)))
				advances.append(0)
				clicks = clicks - 1
			elif( selection is "2" ) :
				print(server)
				print("Which server? (0-index, left to right)")
				server_selection = raw_input()
				print(hand)
				print("Which hand? (0-index, left to right)")
				hand_selection = raw_input()
				server[int(server_selection)].append(hand.pop(int(hand_selection)))
				clicks = clicks - 1
			elif( selection is "3" ):
				print(hand)
				print("Which hand? (0-index, left to right)")
				hand_selection = raw_input()
				archives.append(hand.pop(int(hand_selection)))
				clicks = clicks - 1
			elif( selection is "4" ):
				print(server)
				print("Which server? (0-index, left to right)")
				server_selection = raw_input()
				print(hand)
				print("Which hand? (0-index, left to right)")
				hand_selection = raw_input()
				upgrades[int(server_selection)].append(hand.pop(int(hand_selection)))
				clicks = clicks - 1
			else:
				print("Not an option")
		elif(selection is "3"):
			print(server)
			print("Which server? (0-index, left to right)")
			selection = raw_input()
			advances[int(selection)] = advances[int(selection)] + 1
			clicks = clicks - 1
		elif(selection is "4"):
			print(server)
			print("Which server? (0-index, left to right)")
			selection = raw_input()
			archives.append(server.pop(int(selection)))
		elif(selection is "5"):
			print("How many cards?")
			selection = raw_input()
			print(deck[0:int(selection)])
		elif(selection is "6"):
			print(archives)
		else:
			print("Not an option.")
	print("Player 2's turn")
	raw_input()
	hand.append(deck.pop())
	clicks = 3
