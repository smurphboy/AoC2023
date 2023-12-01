import re

with open('Day01/input.txt') as f:
    lines = [line for line in f]

rowvals = []

for line in lines:
    digits = [int(i) for i in list(line) if i.isdigit()]
    rowvals.append(digits[0]*10+digits[-1])

print('Part One:', sum(rowvals))

rowvals2 = []
for line in lines:
    digits = []
    linelist = list(line)
    for idx in range(len(linelist)):
        if linelist[idx].isdigit():
            digits.append(linelist[idx])
        if linelist[idx:idx+3] == list('one'):
            digits.append('1')
        if linelist[idx:idx+3] == list('two'):
            digits.append('2')
        if linelist[idx:idx+5] == list('three'):
            digits.append('3')
        if linelist[idx:idx+4] == list('four'):
            digits.append('4')       
        if linelist[idx:idx+4] == list('five'):
            digits.append('5')
        if linelist[idx:idx+3] == list('six'):
            digits.append('6')
        if linelist[idx:idx+5] == list('seven'):
            digits.append('7')
        if linelist[idx:idx+5] == list('eight'):
            digits.append('8')
        if linelist[idx:idx+4] == list('nine'):
            digits.append('9')
    rowvals2.append(int(digits[0])*10+int(digits[-1]))
print('Part Two:', sum(rowvals2))