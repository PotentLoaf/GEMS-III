#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:47:59 2018

@author: stem
"""

import random
#add stats to level up
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
moves = {'Tackle' : {'power' : 35, 'type' : 'normal', 'message' : 'x tackled the opponent with all its might!', 'status' : none}, \
'Splash' : {'power' : 0, 'type' :  'water', 'message' : 'the wild x used splash!  But splash did nothing!', 'status' : none}, \
'Ice Beam' : {'power' : 90, 'type' : 'ice', 'message' : 'the wild x used ice beam!', 'status' : freeze},  \
'Peck' : {'power' : 35, type : 'normal', 'message' : 'the wild x used peck!', 'status' : none}, \
'Leech Seed' : {'power' : 0, 'type' :'grass', 'message' : 'the wild x used leech seed!', 'status' :  seed} ,  \
'Scratch' : {'power' : 40, 'type' : 'normal', 'message' : 'the wild x used scratch!', 'status' : none}, \
'Synthesis': {'power' : 0, 'type' : 'grass', 'message' : 'x used synthesis!', 'status' : none}, \
'Rock Throw': {'power' : 50, 'type' : 'rock', 'message' : 'x used rock throw!', 'status' : none}, \
'Ember' : {40, 'fire', 'the wild x used ember!', burn},\
'Smack Down' : {'power' : 50, 'type' : 'rock', 'message' : 'the wild x used smack down!', 'status' : none}, \
'Bite' : {'power': 38, 'type': 'dark', 'message' : 'the wild x used bite!', 'status' : none}}
spearow ={'name': 'Spearow', 'health' : 31, 'attack' : 23, 'defense' : 22, 'speed' : 35, 'exp' : 800, 'level' : 8, 'moves' : {'Peck' : 35}}
caterpie ={'name': 'Caterpie', 'health' : 32, 'attack' : 20, 'defense' : 18, 'speed' : 36, 'exp' : 900, 'level' : 9, 'moves' : {'Tackle' : 35}}
oddish ={'name': 'Oddish', 'health' : 34, 'attack' : 30, 'defense' : 22,'speed' : 35, 'exp' : 1000, 'level' : 10, 'moves' : {'Leech Seed' : 0, 'Absorb' : 20}}
pidgey = {'name' : 'Pidgey', 'health' : 28, 'max health' : 28, 'attack' : 20, 'defense' : 20, 'speed' : 30, 'exp' : 500, 'level' : 5, 'moves' : {'Tackle' : 35}} 
pikachu = {'name' : 'Pikachu' ,  'health' : 30, 'max health' : 30, 'attack' : 25, 'defense' : 23, 'speed' : 40, 'exp' : 500, 'level' : 5, 'moves' : {'Thundershock' : 40}}
charmander = {'name' : 'Charmander' ,  'health' : 35, 'max health' : 35, 'attack' : 28, 'defense' : 25, 'speed' : 28, 'exp' : 500, 'level' : 5, 'moves' : {'Scratch' : 40}}
squirtle = {'name' : 'Squirtle' ,  'health' : 38, 'max health' : 38, 'attack' : 25, 'defense' : 30, 'speed' : 28, 'exp' : 500, 'level' : 5, 'moves' : {'Tackle' : 35}}
bulbasaur = {'name' : 'Bulbasaur' ,  'health' : 35, 'max health' : 35, 'attack' : 25, 'defense' : 28, 'speed' : 30, 'exp' : 500, 'level' : 5, 'moves' : {'Tackle' : 35}}


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

def run(p1, p2):
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
        p['']
    else:
        p['level'] = a
    

def battle(p1, p2):
    print('---', pName,"'s Turn---")
    displayHealth(p1, p2)
    print('What will ', p1['name'], ' do?')
    print('1. Attack')
    print('2. Run')
    choice= int(input('Enter your choice: '))
    if choice == 1:
        print('---',p1['name'], "'s Moves---")
        y = 1
        for x in p1['moves']:
            print(y,'. ',x)
        moveChoice = int(input('Enter your move: '))
        attack(p1, p2, moveChoice)
        displayHealth(p1, p2)
        if(p1['health'] > 0 and p2['health'] > 0):
            print('---',p2['name'], "'s Turn---")
            attackBot(p2, p1)
    elif choice == 2:
        print('You couldn''t get away!')
        if(p1['health'] > 0 and p2['health'] > 0):
            print('---',p2['name'],"s Turn---")
            attackBot(p2, p1)
    else:
        print("Invalid move.")

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
#clean(pokemon[0])

while pokemon[0]['health'] > 0 and pidgey['health'] > 0:
    battle(pokemon[0],pidgey)
    
if pokemon[0]['health'] > 0:        
    print('You defeated Pidgey!')
    expUp(pokemon[0],50)
else:
    print('Pidgey defeated you! You rush your pokemon to the pokecenter...')


print('After you defeat the wild Pidgey, you continue on route 20 to Viridian City as you journey through another patch of tall grass.  Suddenly, a wild Sentret appears from the grass!')	
 


sentret = {'health' : 25, 'attack' : 10, 'defense' : 5} 
print('After you defeated the wild Sentret, you arrive at Viridian City.')
print('1. Go to the pokemon center and heal your pikachu.')
print('2. Go to the pokemart and buy some pokeballs and potions.')
print('3. Go home')
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
    else:
        print('Invalid choice.')
print('You then decide to walk around and explore . While exploring, you bump into another trainer named Ian and he challenges you to your first trainer battle!')

sentret = {'health' : 25, 'attack' : 10, 'defense' : 5} 
print('After you defeated the wild Sentret, you arrive at Viridian City.')
print('1. Go to the pokemon center and heal your pikachu.')
print('2. Go to the pokemart and buy some pokeballs and potions.')
print('3. Go home')
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
    else:
        print('Invalid choice.')
print('You then decide to walk around and explore Viridian City. While exploring, you bump into another trainer named Ian and he challenges you to your first trainer battle!')


while pokemon[0]['health'] > 0 and oddish['health'] > 0:
    battle(pokemon[0],oddish)

print("Brock, the evil rock type gym leader challenges you to your fist major pokemon battle against a trainer!!!  You must accept as he threatens to kidnap your powerful starter pokemon!  Prove yourself for your and your pokemon's sakes!")
while pokemon[0]['health'] > 0 and geodude['health'] > 0:
    battle(pokemon[0],geodude)
