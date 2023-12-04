import math

with open('Day04/input.txt') as f:
    rows = [line for line in f]

# print(rows)
totalscore = 0
cards = 0
cardscores = {}
totalcards = {}
for card in rows:
    cards += 1
    totalcards[cards] = 1
cards = 0
for card in rows:
    hand = card.split(':')
    winners = (set(filter(None, hand[1].split('|')[0].strip().split(' '))))
    numbers = (set(filter(None, hand[1].split('|')[1].strip().split(' '))))
    scoring = set.intersection(winners, numbers)
    if len(scoring) != 0:
        score = pow(2,len(scoring)-1)
        totalscore += pow(2,len(scoring)-1)
    else: score = 0
    cards += 1
    cardscores[cards] = score
    for extra in range(len(scoring)):
        idx = int(cards+extra+1)
        totalcards[idx] = totalcards.get(idx,1) + totalcards.get(cards,1)

print('Part One:', totalscore)
print('Part Two:', sum(totalcards.values()))