SPADE=SPADES='\u2660'
DIAMOND=DIAMONDS='\u2666'
CLUB=CLUBS='\u2663'
HEART=HEARTS='\u2665'

def strCard(card):
    out=f'+{"-"*9}+\n'
    if card:
        out+=f'|{card[0]}{" "*(8-len(card[0]))}{card[1]}|\n'
        if card[0]=='A':
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*9}|\n'
        elif card[0]=='2':
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
        elif card[0]=='3':
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
        elif card[0]=='4':
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
        elif card[0]=='5':
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
        elif card[0]=='6':
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
        elif card[0]=='7':
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*9}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
        elif card[0]=='8':
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
        elif card[0]=='9':
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*4}{card[1]}{" "*4}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
        elif card[0]=='10':
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
            out+=f'|{" "*3}{card[1]} {card[1]}{" "*3}|\n'
        elif card[0]=='J':
            out+=f'|    ww   |\n'
            out+=f'|    {{)   |\n'
            out+=f'|    {card[1]}    |\n'
            out+=f'|    {card[1]}    |\n'
            out+=f'|   {card[1]}{card[1]}[   |\n'
        elif card[0]=='Q':
            out+=f'|    ww   |\n'
            out+=f'|    {{(   |\n'
            out+=f'|    {card[1]}{card[1]}   |\n'
            out+=f'|   {card[1]}{card[1]}{card[1]}   |\n'
            out+=f'|   {card[1]}{card[1]}O   |\n'
        elif card[0]=='K':
            out+=f'|    WW   |\n'
            out+=f'|    {{)   |\n'
            out+=f'|    {card[1]}{card[1]}   |\n'
            out+=f'|   {card[1]}{card[1]}{card[1]}   |\n'
            out+=f'|   {card[1]}{card[1]}>   |\n'
        out+=f'|{card[1]}{" "*(8-len(card[0]))}{card[0]}|\n'
    else:
        out+=f'|{" "*9}|\n'
        out+=f'|  +---+  |\n'
        out+=f'|  |   |  |\n'
        out+=f'|  | O |  |\n'
        out+=f'|  |   |  |\n'
        out+=f'|  +---+  |\n'
        out+=f'|{" "*9}|\n'
    return out+f'+{"-"*9}+\n'

def strHand(hand):
    cardLines=[strCard(card).split('\n') for card in hand]
    out=''
    for line in range(9):
        out+='   '.join([card[line] for card in cardLines])+'\n'
    return out

print(strHand([('A',SPADES),('3',HEARTS),('J',DIAMONDS),('9',HEARTS),None]))