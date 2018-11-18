# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:30:07 2018

@author: Michael
"""

import random

def makecard():
    '''
    This function creates randomized bingo cards
    '''
    B_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    I_numbers = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    N_numbers = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
    G_numbers = [46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    O_numbers = [61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]
    card = {'b':[],'i':[],'n':[],'g':[],'o':[]}
    while len(card['b']) < 5:
        number = random.choice(B_numbers)
        card['b'].append(number)
        B_numbers.remove(number)
        number = random.choice(I_numbers)
        card['i'].append(number)
        I_numbers.remove(number)
        number = random.choice(N_numbers)
        card['n'].append(number)
        N_numbers.remove(number)
        number = random.choice(G_numbers)
        card['g'].append(number)
        G_numbers.remove(number)
        number = random.choice(O_numbers)
        card['o'].append(number)
        O_numbers.remove(number)
    card['n'][2] = 0    
    return card

def multicard(n):
    '''
    This function makes n number of cards, usually user inputted.
    '''
    game = {}
    for i in range(n):
        game[i] = makecard()
    return game

def printcard(card):
    '''
    This function prints the cards in an easier to understand grid
    '''
    print('B\t I\t N\t G\t O\t')
    print('------------------------------------')
    for i in range(5):
        print(card['b'][i],'\t',card['i'][i],'\t',card['n'][i],'\t',card['g'][i],'\t',card['o'][i],'\t',)
    print('\n')

def is_winner(card):
    '''
    This function checks an individual card for it's win condition; 5 called numbers in a row
    '''
    if sum(card['b']) == 0:
        return True
    elif sum(card['i']) == 0:
        return True
    elif sum(card['n']) == 0:
        return True
    elif sum(card['g']) == 0:
        return True
    elif sum(card['o']) == 0:
        return True
    elif card['b'][0] + card['i'][1] + card['n'][2] + card['g'][3] + card['o'][4] == 0:
        return True
    elif card['b'][4] + card['i'][3] + card['n'][2] + card['g'][1] + card['o'][0] == 0:
        return True
    for i in range(5):
        if card['b'][i] + card['i'][i] + card['n'][i] + card['g'][i] + card['o'][i] == 0:
            return True
    return False

uncalled_numbers = list(range(1,76)) #creates a list of all bingo numbers
called_numbers = [] 
user_input = int(input('How many cards would you like to play?'))
fullgame = multicard(user_input) #generates a user inputted number of bingo cards to play
endgame = fullgame.copy() #creating a copy of above so that initial conditions are saved.

for i in range(user_input): #prints all of the bingo cards in play
    printcard(fullgame[i])
    
def endcon(u_inp,game):
    '''
    This funciton checks if any of the cards meet the win condition
    '''
    for i in range(u_inp):
       if is_winner(endgame[i]):
           return True

#The below block is a loop that ends when a card gets BINGO.
#It checks to see if each card has the number, and if so, replaces it with 0
        
while True:    
    if endcon(user_input,endgame):
        break
    number = random.choice(uncalled_numbers)
    for i in range(user_input):
        for n, x in enumerate(endgame[i]['b']):
            if x == number:
                endgame[i]['b'][n] = 0
        
        for n, x in enumerate(endgame[i]['i']):
            if x == number:
               endgame[i]['i'][n] = 0
        
        for n, x in enumerate(endgame[i]['n']):
            if x == number:
                endgame[i]['n'][n] = 0
        
        for n, x in enumerate(endgame[i]['g']):
            if x == number:
                endgame[i]['g'][n] = 0
        
        for n, x in enumerate(endgame[i]['o']):
            if x == number:
                endgame[i]['o'][n] = 0    
    called_numbers.append(number)
    uncalled_numbers.remove(number)


print('The numbers called were:', called_numbers)
print('The numbers left uncalled were:', uncalled_numbers)
print('The final cards looked like this:')        
for i in range(user_input):
    printcard(endgame[i])


        

