import string

specchars = set(string.printable) - set(string.ascii_letters) - set("1234567890.")

def part(candidate):
    '''returns True is number is surrounded by a symbol. Expectes a candidate with 
    an x,y tuple for the start and end of the number'''
    # print(candidate, candidate[2][0])
    if candidate[0][0] != 0: # left ends
        leftend = grid[int(candidate[0][1])][int(candidate[0][0]) - 1]
        if set(leftend).intersection(specchars): #we have a symbol
            # print('leftend', candidate[1])
            return True
    if candidate[2][0] != linelen-1: # right ends
        rightend = grid[int(candidate[2][1])][int(candidate[2][0])]
        if set(rightend).intersection(specchars): #we have a symbol
            # print('rightend', candidate[1])
            return True
    checkcells = []
    if candidate[0][1] != 0: # aboves
        if candidate[0][0] != 0: # look above and left
            if candidate[2][0] != linelen-1: # middle (+2)          
                for idx in range(candidate[2][0]-candidate[0][0]+2): 
                    checkcells.append(grid[candidate[0][1]-1][candidate[0][0]+idx-1])
            else: # right hand end (+1 r)
                for idx in range(candidate[2][0] - candidate[0][0]+1): 
                    checkcells.append(grid[candidate[0][1]-1][candidate[0][0]+idx-1])
        else: #left hand end 
            for idx in range(candidate[2][0] - candidate[0][0]+1): 
                checkcells.append(grid[candidate[0][1]-1][candidate[0][0]+idx])
        for cell in checkcells: #now we check for symbols
            if set(cell).intersection(specchars): # we have a symbol
                # print('above', candidate[1])
                return True
    checkcells = []
    if candidate[2][1] != gridheight-1: # belows
        if candidate[0][0] != 0: # look above and left
            if candidate[2][0] != linelen-1: # middle (+2)          
                for idx in range(candidate[2][0]-candidate[0][0]+2): 
                    checkcells.append(grid[candidate[0][1]+1][candidate[0][0]+idx-1])
            else: # right hand end (+1 r)
                for idx in range(candidate[2][0] - candidate[0][0]+1): 
                    checkcells.append(grid[candidate[0][1]+1][candidate[0][0]+idx-1])
        else: #left hand end 
            for idx in range(candidate[2][0] - candidate[0][0]+1): 
                checkcells.append(grid[candidate[0][1]+1][candidate[0][0]+idx])
        for cell in checkcells: #now we check for symbols
            if set(cell).intersection(specchars): # we have a symbol
                # print('below', candidate[1])
                return True
            
with open('Day03/input.txt') as f:
    grid = [list(line) for line in f]
    linelen = len(grid[0])
    gridheight = len(grid)
    # print(linelen, gridheight)


# First we scan for sequences of numbers
partnos = []

for idy, line in enumerate(grid):
    candidate = []
    partial = ''
    for idx, cell in enumerate(line):
        if cell.isnumeric():
            if partial == '': # found the start of a candidate part number
                candidate.append((idx, idy))
            partial+= cell
        else:
            if partial != '': # found the end of a candidate part number
                candidate.append(partial)
                candidate.append((idx, idy))
                partial = ''
                # is it a part number?
                if part(candidate):
                    partnos.append(int(candidate[1]))
                candidate = []


print('Part One:',sum(partnos))