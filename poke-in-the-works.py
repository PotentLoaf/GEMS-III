#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:47:59 2018

@author: stem
"""
import time
import random
#add stats to level up
#add possible moves
#speed
#catch
#items
#moves option
#what it does
#types
#status
#picture
#sound
#dual types

#power, type, 'message', 'status'

#status
none = 1
freeze = 2
burn = 3
seed = 4
#moves
moves = {'Tackle' : {'name' : 'Tackle','power' : 35, 'type' : 'normal', 'message' : 'x tackled the opponent with all its might!', 'status' : none}, \
'Splash' : {'name' : 'Splash','power' : 0, 'type' :  'water', 'message' : 'the wild x used splash!  But splash did nothing!', 'status' : none}, \
'Ice Beam' : {'name' : 'Ice Beam','power' : 90, 'type' : 'ice', 'message' : 'the wild x used ice beam!', 'status' : freeze},  \
'Peck' : {'name' : 'Peck','power' : 35, 'type' : 'normal', 'message' : 'the wild x used peck!', 'status' : none}, \
'Leech Seed' : {'name' : 'Leech Seed','power' : 0, 'type' :'grass', 'message' : 'the wild x used leech seed!', 'status' :  seed} ,  \
'Scratch' : {'name' : 'Scratch','power' : 40, 'type' : 'normal', 'message' : 'the wild x used scratch!', 'status' : none}, \
'Synthesis': {'name' : 'Synthesis','power' : 0, 'type' : 'grass', 'message' : 'x used synthesis!', 'status' : none}, \
'Rock Throw': {'name' : 'Rock Throw','power' : 50, 'type' : 'rock', 'message' : 'x used rock throw!', 'status' : none}, \
'Smack Down' : {'name' : 'Smack Down','power' : 50, 'type' : 'rock', 'message' : 'the wild x used smack down!', 'status' : none}, \
'Bite' : {'name' : 'Bite','power': 38, 'type': 'dark', 'message' : 'the wild x used bite!', 'status' : none},\
'Ember' : {'name' : 'Ember','power': 40, 'type': 'fire', 'message' : 'the x used ember!', 'status' : burn},\
#"Rock Tomb" : {'power' : 50, 'type': 'rock', 'message' : 'Brock’s x used rock tomb!', 'status' : none}, \ 
#'Stone Edge' : {'power': 100, 'type': 'rock', 'message' : 'Brock’s x used stone edge!', 'status': none}, \
'Thundershock' : {'name' : 'Thundershock','power': 40, 'type': 'electric', 'message': 'x shocked the opponent!', 'status' : none}}

#pokemon
tackle = frozenset(moves['Tackle'].items())
splash = frozenset(moves['Splash'].items())
iceBeam = frozenset(moves['Ice Beam'].items())
peck = frozenset(moves['Peck'].items())
leechSeed = frozenset(moves['Leech Seed'].items())
scratch = frozenset(moves['Scratch'].items())
synthesis = frozenset(moves['Synthesis'].items())
rockThrow = frozenset(moves['Rock Throw'].items())
smackDown = frozenset(moves['Smack Down'].items())
ember = frozenset(moves['Ember'].items())
bite = frozenset(moves['Bite'].items())
thundershock = frozenset(moves['Thundershock'].items())

growlithe = {'name': 'Growlithe', 'health' : 30, 'max health' : 30, 'attack' : 40, 'defense' : 15, 'speed' : 30,  'exp' : 500, 'level' : 5, 'moves' : {'ember' : 40, 'bite' : 45}, 'desc' : 'Growlithe, a Puppy Pokémon of pleasant demeanor and great diligence. While loyal to its master, it drives enemies away with barks and bites.', 'type' : 'fire'}

seedot ={'name': 'Seedot', 'health' : 23, 'max health' : 23,'attack' : 22, 'defense' : 25, 'speed' : 30, 'exp' : 500, 'level' : 5, 'moves' : {'tackle' : 35},'desc' : 'Seedot, the acorn pokemon. A beige, mask-like pattern covers its large black eyes, and it has two beige feet. It has a gray "cap" with a short stem on top of its head. The stem is used to hang from tree branches in its forest home. While hanging, this Pokémon absorbs moisture and nutrients from the tree until it becomes too heavy and falls to the ground.', 'type' : 'grass'}

geodude ={"name": 'Geodude', 'health' : 30, 'max health' : 30, 'attack' : 25, 'defense' : 50, 'speed' : 20, 'exp' : 500, "level" : 5, "moves" : {'Rock Throw' : 50, 'Smack Down': 45}, "desc" : "Geodude, the Rock Pokémon. Geodude has incredibly high defensive power, making it virtually resistant to any physical attacks.", 'type' : 'rock'}

magikarp ={'name': 'Magikarp', 'health' : 20, 'max health' : 20,'attack' : 10, 'defense' : 22, 'speed' : 40, 'exp' : 500, 'level' : 5, 'moves' : {'Splash' : 0}, 'desc' : 'Magikarp, the Fish Pokémon. Because all Magikarp seem to do is splash around, some consider them weak, but they''re actually a hardy Pokémon that can survive in water no matter how dirty it is.  It jumps very well and can evolve into a powerful Gyarados.', 'type' : 'water'}
                                                                                                                                
marill ={'name' : 'Marill', 'health' : 35, 'max health' : 35,'attack' : 20, 'defense' : 25, 'speed' : 24, 'exp' : 500, 'level' : 5, 'moves' : {'Ice Beam' : 60}, 'desc' : 'Marill, the Aqua Mouse Pokémon. The tip of its tail floats in water, so it can swim in any current no matter how rough.', 'type' : 'water fairy'}

spearow ={'name': 'Spearow', 'health' : 25, 'max health' : 25,'attack' : 23, 'defense' : 22, 'speed' : 30, 'exp' : 500, 'level' : 5, 'moves' : {'Peck' : 45}, 'desc' : 'Unlike Pidgey, Spearow has a terrible attitude. It is very wild and will sometimes attack other Pokémon and humans.', 'type' : 'normal flying'}

caterpie ={'name': 'Caterpie', 'health' : 26, 'max health' : 26,'attack' : 20, 'defense' : 18, 'speed' : 25, 'exp' : 500, 'level' : 5, 'moves' : {'Tackle' : 35}, 'desc' : 'Caterpie, the Worm Pokémon. Caterpie uses the suction cups on its feet to climb trees and feed on its favorite leaves.', 'type' : 'bug'}

oddish ={'name': 'Oddish', 'health' : 25, 'max health' : 25, 'attack' : 25, 'defense' : 22, 'speed' : 22, 'exp' : 500, 'level' : 5, 'moves' : {'Tackle' : 35}, 'desc' : 'Oddish. This Pokémon is typically found roaming the forest, scattering pollen as it walks around.', 'type' : 'grass'}

pidgey = {'name' : 'Pidgey', 'health' : 28, 'max health' : 28, 'attack' : 20, 'defense' : 20, 'speed' : 30, 'exp' : 500, 'level' : 5, 'moves' : {'Tackle' : 35}, 'desc' : 'Pidgey is a Flying Pokémon. Among all the Flying Pokémon, it is the gentlest and easiest to capture. A perfect target for the beginning Pokémon Trainer to test his Pokémon''s skills.', 'type' : 'normal flying'}

pikachu = {'name' : 'Pikachu' ,  'health' : 30, 'max health' : 30, 'attack' : 35, 'defense' : 23, 'speed' : 90, 'exp' : 500, 'level' : 5, 'moves' : {'Thundershock' : 40}, 'desc' : 'Pikachu, the Mouse Pokémon. It can generate electric attacks from the electric pouches located in both of its cheeks.', 'type' : 'electric'}

charmander = {'name' : 'Charmander' ,  'health' : 35, 'max health' : 35, 'attack' : 32, 'defense' : 25, 'speed' : 65, 'exp' : 500, 'level' : 5, 'moves' : {'Ember' : 40}, "desc" : 'Charmander, the Lizard Pokémon. When the tip of Charmander''s tail burns brightly, that indicates it''s in good health.', 'type' : 'fire'}

squirtle = {'name' : 'Squirtle' ,  'health' : 39, 'max health' : 39, 'attack' : 24, 'defense' : 32, 'speed' : 43, 'exp' : 500, 'level' : 5, 'moves' : {'Water Gun': 45}, 'desc' : 'Squirtle. This Tiny Turtle Pokémon draws its long neck into its shell to launch incredible water attacks with amazing range and accuracy. The blasts can be quite powerful.', 'type' : 'water'}

bulbasaur = {'name' : 'Bulbasaur' ,  'health' : 40, 'max health' : 40, 'attack' : 25, 'defense' : 27, 'speed' : 45, 'exp' : 500, 'level' : 5, 'moves' : {'Vine Whip': 45}, 'desc' : 'Bulbasaur, the Seed Pokémon. A young Bulbasaur uses the nutrients from its seed for the energy it needs to grow.', 'type' : 'grass'}



pokemon = []
#above is whatever pokemon u chose!!!!!!!!!!!!!!!!!!!!!! :)
print('The professor is sleeping.  He then suddenly wakes up and sees you.')
print('Hello there! My name is professor Oak and welcome to the world of Pokemon!  Before we start, I have a couple of questions for you to answer.')
print('1. Boy')
print('2. Girl')
gender = int(input('Are you a boy or a girl? '))

pName = input('What is your name? ')
print('You wake one morning in your bed in Pallet town.  Your mom calls you down quickly to get ready to receive your starter pokemon.  But then you realize you had overslept for an hour, and by the time you arrive to professor Oaks lab, all except for four starter pokemon remained.')
print('Professor Oak then lets you choose the final pokemon.')
print('1. Pikachu')
print('2. Charmander')
print('3. Squirtle')
print('4. Bulbasaur')
starterChoice = int(input('Choose your starter: '))
if starterChoice == 1:
    print('You chose Pikachu!')
    pokemon.append(pikachu)
elif starterChoice == 2:
    print('You chose Charmander!')
    pokemon.append(charmander)
elif starterChoice == 3:
    print('You chose Squirtle!  He also got some nice shades on too!')
    pokemon.append(squirtle)
elif starterChoice == 4:
    print('You chose Bulbasaur!')
    pokemon.append(bulbasaur)
else:
    print('Invalid choice.')    
print('As you leave the lab to begin your journey, Professor Oak then warns you about the tall wild grass, telling you that wild pokemon mostly lurk in those areas.')
print('You walk on route 20 to the next city, Viridian City. As you journey through the wild tall grass, a wild Pidgey suddenly appears in front of you in the tall grass!')
print('You send out ', pokemon[0]['name'])

def heal(p):
    for x in p:
        x['health'] = x['max health']

def attack(p1,p2,move):
    dam = (p1['attack'] - p2['defense'])
    if dam < 0:
        dam = p1['attack']/10
    damg = int(dam*(list(p1['moves'].values())[move-1])/50) + random.randint(0,5)
    #here print the message of the move
    print(p1['name'], ' inflicts ', damg, ' with ', (list(p1['moves'].keys())[move-1]),'!')
    p2['health'] -= damg
    if p2['health'] < 0:
        p2['health'] = 0
        
#first_key = list(colors.keys())[0]
#first_val = list(colors.values())[0]

def attackBot(p1,p2):
    move = random.randint(1,len(p1['moves']))
    dam = (p1['attack'] - p2['defense'])
    if dam < 0:
        dam = int(p1['attack']/10)
    damg = int(dam*(list(p1['moves'].values())[move-1])/50) + random.randint(0,5)
    #here print the message of the move
    print(p1['name'], ' inflicts ', damg, ' with ', (list(p1['moves'].keys())[move-1]),'!')
    p2['health'] -= damg
    if p2['health'] < 0:
        p2['health'] = 0

def run():
	runInt = random.randint(0,1)
	if runInt == 0:
		print('Ran away successfully!')
		return True
	else:
		print('Couldn''t run away!')
		return False

def displayHealth(p1, p2):
	print(p1['name'],"'s Health: ", p1['health'], " / ", p1['max health'])
	print(p2['name'],"s Health: ", p2['health'], " / ", p2['max health'])

def expUp(p, exp):
    p['exp'] += exp
    a = int(p['exp']/100)
    print(p['name'],' has earned ', exp, ' exp.')
    if a != p['level']:
        p['level'] = a
        print(p['name'], ' is now level ', a)
        p['health'] += 5
        p['attack'] += 5
        p['defense'] += 5
        p['health'] += 5
        p['speed'] += 5
    else:
        p['level'] = a
    

def battle(p1, p2):
    print('---', pName,"'s Turn---")
    displayHealth(p1, p2)
    print('What will ', p1['name'], ' do?')
    print('1. Attack')
	print('2. Catch')
	print('3. Switch Pokemon')
    print('4. Run')
    choice= int(input('Enter your choice: '))
    if choice == 1:
        print('---',p1['name'], "'s Moves---")
        y = 1
        for x in p1['moves']:
            print(y,'. ',x)
        moveChoice = int(input('Enter your move: '))
        attack(p1, p2, moveChoice)
        displayHealth(p1, p2)
	elif choice == 2:
		catch(p2)
    elif choice == 4:
        if run() == True:
			break
    else:
        print("Invalid move.")
	if(p1['health'] > 0 and p2['health'] > 0):
            print('---',p2['name'], "'s Turn---")
			time.sleep(1)
            attackBot(p2, p1)
def clean(pokemon):
    print("1 = Pet\n2 = Clean")
    choice = int(input("Enter in your choice!!!!!     "))
    if choice == 1:
        print('Your ', pokemon['name'] ,' enjoyed the pet!')
        if pokemon == pikachu:
            print("Pikachu said pika pika in happiness!")
        elif pokemon == charmander:
            print("Charmander said char char to show its enjoyment!")
        elif pokemon == squirtle:
            print("Squirtle said squirtle squirtle in happiness!")
        elif pokemon == bulbasaur:
            print("Bulbasaur said bulba bulba to show its enjoyment!")  
    elif choice == 2:
        print('Your ', pokemon['name'] ,' is nice and squeaky clean!' )
        if pokemon == pikachu:
            print("Pikachu said pika pika in all its cleansed glory!")
        elif pokemon == charmander:
            print("Charmander said char char in annoyment as his little firey tail steamed up all of the tub's water")
        elif pokemon == squirtle:
            print("Squirtle squirted the water everywhere as he happily swam around the tub!")
        elif pokemon == bulbasaur:
            print("Bulbasaur said bulba bulba as he was nice and clean!")
    else:
        print("Invalid choice.")
#

def catch(p):
    print("You threw a pokeball!")
    time.sleep(2)
	print("Shake")
	time.sleep(1)
	print("Shake")
	time.sleep(1)
	if p['health'] < p['max health']/2:
		chance = random.randint(0,1)
	else:
		chance = random.randint(0,2)
    if chance == 0:
		print("Shake")
		time.sleep(1)
    	print("Congratulations! You have caught ", p['name'],"!")
		pokemon.append(p)
    else:
		print("So close, the pokemon broke out!!!")
		
def switch(p,p2):
	print("Your Pokemon: ")
	count = 1
	healthyP = []
	order = []
	for x in p:
		if x['health'] > 0:
			healthyP.append(x)
			order.append(count)
			print(count,". ", x['name'])
			count += 1
	choice = input("Enter the pokemon to switch in with the current one.")
	battle(healthyP[choice-1], p2)
	print("Go, ",healthyP[choice-1]['name'] , "!") #THIS PROBABLY WON'T WORK
while pokemon[0]['health'] > 0 and pidgey['health'] > 0:
    battle(pokemon[0],pidgey)
    
if pokemon[0]['health'] > 0:        
    print('You defeated Pidgey!')
    expUp(pokemon[0],150)
else:
    print('Pidgey defeated you! You rush your pokemon to the pokecenter...')


print('After you defeat the wild Pidgey, you continue on route 20 to Viridian City as you journey through another patch of tall grass.  Suddenly, a wild Growlithe appears from the grass!')	
 
while pokemon[0]['health'] > 0 and growlithe['health'] > 0:
	battle(pokemon[0],growlithe)


print('After you defeated the wild Growlithe, you arrive at Viridian City.')
print('1. Go to the pokemon center and heal your pikachu.')
print('2. Go to the pokemart and buy some pokeballs and potions.')
print('3. Go home')
print("4. Clean your pokemon")
go = 0
while go != 1 and go != 2:
    go = int(input('Where do you want to go? '))
    if go == 1: 
        print('You go inside the pokemon center and hand your pokemon to nurse joy.  She then heals them and gives it back to you.  You then leave back outside.')
        heal(pokemon)
    elif go == 2:
        print('You go inside the pokemart to buy some pokeballs and potions.  You have 1,000 dollars.  You spend 250 dollars on 15 pokeballs and 20 potions.  You then go back outside.')
    elif go == 3:
        print('You got no home.')
    elif go == 4:
        clean(pokemon[0])
    else:
        print('Invalid choice.')
print('You then decide to walk around and explore Viridian City. While exploring, you bump into another trainer named Ian and he challenges you to your first trainer battle!')


while pokemon[0]['health'] > 0 and oddish['health'] > 0:
    battle(pokemon[0],oddish)
print("After the exhausting battle, you head to the nearby hotel to rest. Out of nowhere, a Seedot falls on top of your head and you discover gravity.")
print("Achievement earned: Discovered Gravity")
time.sleep(1)
while pokemon[0]['health'] > 0 and seedot['health'] > 0:
	battle(pokemon[0],seedot)

print("You finally head to the hotel after a long day's work.")
print("Sleeping...")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
heal(pokemon)

print("You wake up refreshed and head to the gym to fight the gym leader who you heard has been ruling over the city as a dictator.")
time.sleep(2)
print("Brock, the evil rock type gym leader challenges you to your fist major pokemon battle against a trainer!!!  You must accept as he threatens to kidnap your pokemon!  Prove yourself for your and your pokemon's sakes!")
while pokemon[0]['health'] > 0 and geodude['health'] > 0:
    battle(pokemon[0],geodude)
while pokemon[0]['health'] > 0 and oddish['health'] > 0:
    battle(pokemon[0],oddish)

print("Mwahahahaha!  I’ve still got my other Geodude for you to go through!  Go, Onix!")
while pokemon[0]['health'] > 0 and geodude['health'] > 0:
    battle(pokemon[0],geodude)

print("Oh no!!  How did you, a measly scrub defeat my supreme pokemon?!!")

print("I'm leaving this town! I knew from the first day I laid eyes upon it that it was nothing but trash.")
print('You have saved the town! Story Mode Complete.')
print("Created by: Anthony Ma, Brian Ma, and Adrian Ng!")
print("Please purchase the next Pokemon Gems DLC 'The Adventure Continues…'")
print("To continue your wondrous journey, arriving in stores near you this Christmas!")


print("Would you like to continue this game?   \
1. Continue or 2. Stop")
choice= int(input('Enter your choice:  '))
if choice == 1:
    print('1. Go to the pokemon center and heal your pikachu.')
    print('2. Go to the pokemart and buy some pokeballs and potions.')
    print('3. Go home')
    print("4. Clean your pokemon")
    go = 0
    while go != 1 and go != 2:
        go = int(input('Where do you want to go? '))
        if go == 1: 
            print('You go inside the pokemon center and hand your pokemon to nurse joy.  She then heals them and gives it back to you.  You then leave back outside.')
            heal(pokemon)
        elif go == 2:
            print('You go inside the pokemart to buy some pokeballs and potions.  You have 1,000 dollars.  You spend 250 dollars on 15 pokeballs and 20 potions.  You then go back outside.')
        elif go == 3:
            print('You got no home.')
        elif go == 4:
            clean(pokemon[0])
        else:
            print('Invalid choice.')
            
        print("You wandered in the grass and suddenly, a wild Spearow appeared!")
        while pokemon[0]['health'] > 0 and spearow['health'] > 0:
            battle(pokemon[0],spearow)
        
        print("A big Seedot fell out of the tree and hit you on the head!")
        while pokemon[0]['health'] > 0 and seedot['health'] > 0:
            battle(pokemon[0],seedot)
        
        print("You decided to go for a swim in the ocean!")
        while pokemon[0]['health'] > 0 and marill['health'] > 0:
            battle(pokemon[0],marill)
        
        print("Bam!  A crazy magikarp slapped ya in the face!")
        while pokemon[0]['health'] > 0 and magikarp['health'] > 0:
            battle(pokemon[0],magikarp)
        
        print("Wow that was some great training for your pokemon!  \
        You went back into town!")
        
        print("A caterpie blocks your way!")
        
        while pokemon[0]['health'] > 0 and caterpie['health'] > 0:
            battle(pokemon[0],caterpie)
        
elif choice == 2:
    print("BYE")
else:
    print("ok")

