import os
import random
import time

WIDTH=os.get_terminal_size().columns
HEIGHT=os.get_terminal_size().lines-1

SPADE=SPADES='\u2660'
DIAMOND=DIAMONDS='\u2666'
CLUB=CLUBS='\u2663'
HEART=HEARTS='\u2665'

class Card:
    def __init__(self,rank=None,suit=None,x=0,y=0,isHorizontal=False):
        self.rank=rank
        self.suit=suit
        self.x=x
        self.y=y
        self.isHorizontal=isHorizontal

    def getCardGrid(self):
        if not self.isHorizontal:
            grid=[f'+{"-"*9}+']
            if self.rank and self.suit:
                grid+=[f'|{self.rank}{" "*(8-len(self.rank))}{self.suit}|']
                if self.rank=='A':
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|{" "*9}|']
                elif self.rank=='2':
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|    {self.suit}    |']
                elif self.rank=='3':
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|    {self.suit}    |']
                elif self.rank=='4':
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                elif self.rank=='5':
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                elif self.rank=='6':
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                elif self.rank=='7':
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|{" "*9}|']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                elif self.rank=='8':
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                elif self.rank=='9':
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                elif self.rank=='10':
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                    grid+=[f'|   {self.suit} {self.suit}   |']
                elif self.rank=='J':
                    grid+=[f'|    ww   |']
                    grid+=[f'|    {{)   |']
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|    {self.suit}    |']
                    grid+=[f'|   {self.suit}{self.suit}[   |']
                elif self.rank=='Q':
                    grid+=[f'|    ww   |']
                    grid+=[f'|    {{(   |']
                    grid+=[f'|    {self.suit}{self.suit}   |']
                    grid+=[f'|   {self.suit}{self.suit}{self.suit}   |']
                    grid+=[f'|   {self.suit}{self.suit}O   |']
                elif self.rank=='K':
                    grid+=[f'|    WW   |']
                    grid+=[f'|    {{)   |']
                    grid+=[f'|    {self.suit}{self.suit}   |']
                    grid+=[f'|   {self.suit}{self.suit}{self.suit}   |']
                    grid+=[f'|   {self.suit}{self.suit}>   |']
                grid+=[f'|{self.suit}{" "*(8-len(self.rank))}{self.rank}|']
            else:
                grid+=[f'|{" "*9}|']
                grid+=[f'|  +---+  |']
                grid+=[f'|  |   |  |']
                grid+=[f'|  | O |  |']
                grid+=[f'|  |   |  |']
                grid+=[f'|  +---+  |']
                grid+=[f'|{" "*9}|']
            grid+=[f'+{"-"*9}+']
        else:
            
# +-------------------+
# |♥                 2|
# |    ♥         ♥    |
# |2                 ♥|
# +-------------------+
            grid=[f'+{"-"*15}+']
            if self.rank and self.suit:
                if self.rank!='J' and self.rank!='Q' and self.rank!='K':
                    grid+=[f'|{self.suit}{" "*(14-len(self.rank))}{self.rank}|']
                    if self.rank=='A':
                        grid+=[f'|{" "*15}|']
                        grid+=[f'|       {self.suit}       |']
                        grid+=[f'|{" "*15}|']
                    elif self.rank=='2':
                        grid+=[f'|{" "*15}|']
                        grid+=[f'|   {self.suit}       {self.suit}   |']
                        grid+=[f'|{" "*15}|']
                    elif self.rank=='3':
                        grid+=[f'|{" "*15}|']
                        grid+=[f'|   {self.suit}   {self.suit}   {self.suit}   |']
                        grid+=[f'|{" "*15}|']
                    elif self.rank=='4':
                        grid+=[f'|   {self.suit}       {self.suit}   |']
                        grid+=[f'|{" "*15}|']
                        grid+=[f'|   {self.suit}       {self.suit}   |']
                    elif self.rank=='5':
                        grid+=[f'|   {self.suit}       {self.suit}   |']
                        grid+=[f'|       {self.suit}       |']
                        grid+=[f'|   {self.suit}       {self.suit}   |']
                    elif self.rank=='6':
                        grid+=[f'|   {self.suit}   {self.suit}   {self.suit}   |']
                        grid+=[f'|{" "*15}|']
                        grid+=[f'|   {self.suit}   {self.suit}   {self.suit}   |']
                    elif self.rank=='7':
                        grid+=[f'|   {self.suit}   {self.suit}   {self.suit}   |']
                        grid+=[f'|     {self.suit}{" "*9}|']
                        grid+=[f'|   {self.suit}   {self.suit}   {self.suit}   |']
                    elif self.rank=='8':
                        grid+=[f'|   {self.suit}   {self.suit}   {self.suit}   |']
                        grid+=[f'|     {self.suit}   {self.suit}     |']
                        grid+=[f'|   {self.suit}   {self.suit}   {self.suit}   |']
                    elif self.rank=='9':
                        grid+=[f'|   {self.suit} {self.suit}   {self.suit} {self.suit}   |']
                        grid+=[f'|       {self.suit}       |']
                        grid+=[f'|   {self.suit} {self.suit}   {self.suit} {self.suit}   |']
                    elif self.rank=='10':
                        grid+=[f'|   {self.suit} {self.suit} {self.suit} {self.suit} {self.suit}   |']
                        grid+=[f'|{" "*15}|']
                        grid+=[f'|   {self.suit} {self.suit} {self.suit} {self.suit} {self.suit}   |']
                    grid+=[f'|{self.rank}{" "*(14-len(self.rank))}{self.suit}|']
                elif self.rank=='J':
                    grid+=[f'|{self.suit}      ww     J|']
                    grid+=[f'|       {{)      |']
                    grid+=[f'|       {self.suit}       |']
                    grid+=[f'|       {self.suit}       |']
                    grid+=[f'|J     {self.suit}{self.suit}[     {self.suit}|']
                elif self.rank=='Q':
                    grid+=[f'|{self.suit}      ww     Q|']
                    grid+=[f'|       {{(      |']
                    grid+=[f'|       {self.suit}{self.suit}      |']
                    grid+=[f'|      {self.suit}{self.suit}{self.suit}      |']
                    grid+=[f'|Q     {self.suit}{self.suit}O     {self.suit}|']
                elif self.rank=='K':
                    grid+=[f'|{self.suit}      WW     K|']
                    grid+=[f'|       {{)      |']
                    grid+=[f'|       {self.suit}{self.suit}      |']
                    grid+=[f'|      {self.suit}{self.suit}{self.suit}      |']
                    grid+=[f'|K     {self.suit}{self.suit}>     {self.suit}|']
            else:
                grid+=[f'|{" "*15}|']
                grid+=[f'|   +-------+   |']
                grid+=[f'|   |   O   |   |']
                grid+=[f'|   +-------+   |']
                grid+=[f'|{" "*15}|']
            grid+=[f'+{"-"*15}+']
        return [list(line) for line in grid]

    def getWidth(self):
        return 11 if not self.isHorizontal else 9

    def getHeight(self):
        return 9 if not self.isHorizontal else 11

    def copy(self):
        return Card(self.rank,self.suit,self.x,self.y,self.isHorizontal)

def newDeck():
    return [Card(rank,suit) for suit in [SPADES,DIAMONDS,CLUBS,HEARTS] for rank in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']]

def printCards(hand):
    grid=[[' ']*WIDTH for line in range(HEIGHT)]
    for card in hand:
        for row,line in enumerate(card.getCardGrid()):
            for col,char in enumerate(line):
                if 0<=row+card.y<HEIGHT and 0<=col+card.x<WIDTH: # (x,y) is converted to (row,col) for printing
                    grid[row+card.y][col+card.x]=char
    out='\n'.join([''.join(line) for line in grid])
    os.system('cls' if os.name=='nt' else 'clear')
    print(out)

hand=[]
for index,card in enumerate((newDeck()[:13])):
    a=card
    b=a.copy()
    a.y=index*a.getHeight()
    b.x=a.getWidth()
    b.y=index*a.getHeight()
    b.isHorizontal=True
    hand.append(a)
    hand.append(b)
printCards(hand)