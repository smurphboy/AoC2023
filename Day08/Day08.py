with open('Day08/input.txt') as f:
    rows = [line for line in f]

instructs = list(rows[0].strip())
steps = {}
for idx, step in enumerate(rows):
    if idx >= 2:
        if idx == 2:
            initalstep = step[0:3]
        steps[step[0:3]] = [step[7:10], step[12:15]]
print(instructs)
print(len(instructs))
print(initalstep)
currentstep = initalstep
instructstep = 0
stepcount = 0
loop = 0
while loop < 286:
    if instructs[instructstep%(len(instructs))] == 'L':
        currentstep = steps[currentstep][0]
    else:
        currentstep = steps[currentstep][1]
    stepcount += 1
    if currentstep == 'ZZZ':
        break
    print(instructstep,':', instructs[(instructstep%(281))] , ':',currentstep)
    instructstep += 1
    loop += 1

print(stepcount)

