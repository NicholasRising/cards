import os
import random
import time

SPADE=SPADES='\u2660'
DIAMOND=DIAMONDS='\u2666'
CLUB=CLUBS='\u2663'
HEART=HEARTS='\u2665'

def newDeck():
    deck=[(rank,suit) for rank in ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] for suit in [SPADES,DIAMONDS,CLUBS,HEARTS]]
    random.shuffle(deck)
    return deck

def cardGrid(card):
    grid=[f'+{"-"*9}+']
    if card:
        grid+=[f'|{card[0]}{" "*(8-len(card[0]))}{card[1]}|']
        if card[0]=='A':
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*9}|']
        elif card[0]=='2':
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
        elif card[0]=='3':
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
        elif card[0]=='4':
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
        elif card[0]=='5':
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
        elif card[0]=='6':
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
        elif card[0]=='7':
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*9}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
        elif card[0]=='8':
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
        elif card[0]=='9':
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*4}{card[1]}{" "*4}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
        elif card[0]=='10':
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
            grid+=[f'|{" "*3}{card[1]} {card[1]}{" "*3}|']
        elif card[0]=='J':
            grid+=[f'|    ww   |']
            grid+=[f'|    {{)   |']
            grid+=[f'|    {card[1]}    |']
            grid+=[f'|    {card[1]}    |']
            grid+=[f'|   {card[1]}{card[1]}[   |']
        elif card[0]=='Q':
            grid+=[f'|    ww   |']
            grid+=[f'|    {{(   |']
            grid+=[f'|    {card[1]}{card[1]}   |']
            grid+=[f'|   {card[1]}{card[1]}{card[1]}   |']
            grid+=[f'|   {card[1]}{card[1]}O   |']
        elif card[0]=='K':
            grid+=[f'|    WW   |']
            grid+=[f'|    {{)   |']
            grid+=[f'|    {card[1]}{card[1]}   |']
            grid+=[f'|   {card[1]}{card[1]}{card[1]}   |']
            grid+=[f'|   {card[1]}{card[1]}>   |']
        grid+=[f'|{card[1]}{" "*(8-len(card[0]))}{card[0]}|']
    else:
        grid+=[f'|{" "*9}|']
        grid+=[f'|  +---+  |']
        grid+=[f'|  |   |  |']
        grid+=[f'|  | O |  |']
        grid+=[f'|  |   |  |']
        grid+=[f'|  +---+  |']
        grid+=[f'|{" "*9}|']
    grid+=[f'+{"-"*9}+']
    return [list(line) for line in grid]

def printCards(hand):
    width=os.get_terminal_size().columns
    height=os.get_terminal_size().lines-2
    grid=[[' ']*width for line in range(height)]
    for card,pos in hand:
        for row,line in enumerate(cardGrid(card)):
            for col,char in enumerate(line):
                if 0<=row+pos[1]<height and 0<=col+pos[0]<width: # (x,y) is converted to (row,col) for printing
                    grid[row+pos[1]][col+pos[0]]=char
    os.system('cls' if os.name=='nt' else 'clear')
    for line in grid:
        print(''.join(line))

deck=newDeck()
hand=[(('A',SPADES),(5,7)),(('5',HEARTS),(12,8))]
printCards(hand)