with open('Day05/input.txt') as f:
    rows = [line for line in f]
oseeds = list(rows[0].split(':')[1].strip().split(' '))
origseeds = [eval(i) for i in oseeds]
zone = None
soil = []
fert = []
water = []
light = []
temp = []
humid = []
loc = []
for row in rows:
    if row.strip() == 'seed-to-soil map:':
        zone = 'soil'
    elif row.strip() == 'soil-to-fertilizer map:':
        zone = 'fert'
    elif row.strip() == 'fertilizer-to-water map:':
        zone = 'water'
    elif row.strip() == 'water-to-light map:':
        zone = 'light'
    elif row.strip() == 'light-to-temperature map:':
        zone = 'temp'
    elif row.strip() == 'temperature-to-humidity map:':
        zone = 'humid'
    elif row.strip() == 'humidity-to-location map:':
        zone = 'loc'
    # elif row.isspace():
    #     print('Blank')
    # print(zone)
    if zone == 'soil':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            soil.append([int(x) for x in mapels])
    if zone == 'fert':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            fert.append([int(x) for x in mapels])
    if zone == 'water':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            water.append([int(x) for x in mapels])
    if zone == 'light':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            light.append([int(x) for x in mapels])
    if zone == 'temp':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            temp.append([int(x) for x in mapels])
    if zone == 'humid':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            humid.append([int(x) for x in mapels])
    if zone == 'loc':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            loc.append([int(x) for x in mapels])

# print(sorted(soil, key=lambda two: two[1]))
# print(sorted(fert, key=lambda two: two[1]))
# print(sorted(water, key=lambda two: two[1]))
# print(sorted(light, key=lambda two: two[1]))
# print(sorted(temp, key=lambda two: two[1]))
# print(sorted(humid, key=lambda two: two[1]))
# print(sorted(loc, key=lambda two: two[1]))
seeds = list(range(1,max(origseeds)))

for idx, seed in enumerate(seeds):
    for row in sorted(loc, key=lambda two: two[1]):
        minsource = int(row[1])
        maxsource = int(row[1]) + int(row[2])
        # print(minsource, maxsource, mapels[2])
        # print(seed)
        if int(seeds[idx]) >= minsource and int(seeds[idx]) < maxsource:
            seeds[idx] = int(seeds[idx]) + int(row[0]) - int(row[1])
            break
    for row in sorted(humid, key=lambda two: two[1]):
        minsource = int(row[1])
        maxsource = int(row[1]) + int(row[2])
        # print(minsource, maxsource, mapels[2])
        # print(seed)
        if int(seeds[idx]) >= minsource and int(seeds[idx]) < maxsource:
            seeds[idx] = int(seeds[idx]) + int(row[0]) - int(row[1])
            break
    # print('humid: ',seeds)
    for row in sorted(temp, key=lambda two: two[1]):
        minsource = int(row[1])
        maxsource = int(row[1]) + int(row[2])
        # print(minsource, maxsource, mapels[2])
        # print(seed)
        if int(seeds[idx]) >= minsource and int(seeds[idx]) < maxsource:
            seeds[idx] = int(seeds[idx]) + int(row[0]) - int(row[1])
            break
    # print('temp: ',seeds)
    for row in sorted(light, key=lambda two: two[1]):
        minsource = int(row[1])
        maxsource = int(row[1]) + int(row[2])
        # print(minsource, maxsource, mapels[2])
        # print(seed)
        if int(seeds[idx]) >= minsource and int(seeds[idx]) < maxsource:
            seeds[idx] = int(seeds[idx]) + int(row[0]) - int(row[1])
            break
    # print('light: ',seeds)
    for row in sorted(water, key=lambda two: two[1]):
        minsource = int(row[1])
        maxsource = int(row[1]) + int(row[2])
        # print(minsource, maxsource, mapels[2])
            # print(seed)
        if int(seeds[idx]) >= minsource and int(seeds[idx]) < maxsource:
            seeds[idx] = int(seeds[idx]) + int(row[0]) - int(row[1])
            break
    # print('water: ',seeds)
    for row in sorted(fert, key=lambda two: two[1]):
        minsource = int(row[1])
        maxsource = int(row[1]) + int(row[2])
        # print(minsource, maxsource, mapels[2])
            # print(seed)
        if int(seeds[idx]) >= minsource and int(seeds[idx]) < maxsource:
            seeds[idx] = int(seeds[idx]) + int(row[0]) - int(row[1])
            break
    # print('fert: ',seeds)
    for row in sorted(soil, key=lambda two: two[1]):
        minsource = int(row[1])
        maxsource = int(row[1]) + int(row[2])
        # print(minsource, maxsource, mapels[2])
        # print(seed)
        if int(seeds[idx]) >= minsource and int(seeds[idx]) < maxsource:
            seeds[idx] = int(seeds[idx]) + int(row[0]) - int(row[1])
            break
    # print('soil: ',seeds)
    if seeds[idx] in origseeds:
        print(seeds[idx])

