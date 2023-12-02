import re

with open('Day02/input.txt') as f:
    rows = [line for line in f]

ids = []
powers = []
for row in rows:
    splitrow = re.split('[:;]', row)
    validgame = True
    minred = 0
    mingreen = 0
    minblue = 0
    for hand in splitrow:
        if hand[:4] == 'Game': # game id
            gameid = hand[5:]
            #print(int(gameid))
        else:
            colours = re.split(',', hand)
            #print('new hand')
            red = 0
            green = 0
            blue = 0
            for colour in colours:
#               print('C:', str.split(colour)[1], int(str.split(colour)[0]))
                if str.split(colour)[1] == 'red':
                    red += int(str.split(colour)[0])
                    if red > minred:
                        minred = red
                if str.split(colour)[1] == 'green':
                    green += int(str.split(colour)[0])
                    if green > mingreen:
                        mingreen = green
                if str.split(colour)[1] == 'blue':
                    blue += int(str.split(colour)[0])
                    if blue > minblue:
                        minblue = blue
            if not(red <= 12 and green <= 13 and blue <= 14):
                validgame = False
    if validgame:
        ids.append(int(gameid))
    #print(minred, mingreen, minblue)
    powers.append(minred * mingreen * minblue)
print('Part One:', sum(ids))
print('Part Two:', sum(powers))

