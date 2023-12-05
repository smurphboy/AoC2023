with open('Day05/sample.txt') as f:
    rows = [line for line in f]

seeds = list(rows[0].split(':')[1].strip().split(' '))
print(seeds)
maxseed = max(seeds)
zone = None
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
            minsource = int(mapels[1])
            maxsource = int(mapels[1]) + int(mapels[2])
            # print(minsource, maxsource, mapels[2])
            for idx, seed in enumerate(seeds):
                # print(seed)
                if int(seed) >= minsource and int(seed) < maxsource:
                    seeds[idx] = int(seed) + int(mapels[0]) - int(mapels[1])
    print(seeds)
    if zone == 'fert':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            minsource = int(mapels[1])
            maxsource = int(mapels[1]) + int(mapels[2])
            # print(minsource, maxsource, mapels[2])
            for idx, seed in enumerate(seeds):
                # print(seed)
                if int(seed) >= minsource and int(seed) < maxsource:
                    seeds[idx] = int(seed) + int(mapels[0]) - int(mapels[1])
    print(seeds)
    if zone == 'water':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            minsource = int(mapels[1])
            maxsource = int(mapels[1]) + int(mapels[2])
            # print(minsource, maxsource, mapels[2])
            for idx, seed in enumerate(seeds):
                # print(seed)
                if int(seed) >= minsource and int(seed) < maxsource:
                    seeds[idx] = int(seed) + int(mapels[0]) - int(mapels[1])
    print(seeds)
    if zone == 'light':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            print(mapels)
            minsource = int(mapels[1])
            maxsource = int(mapels[1]) + int(mapels[2])
            print(minsource, maxsource, mapels[2])
            for idx, seed in enumerate(seeds):
                # print(seed)
                if int(seed) >= minsource and int(seed) < maxsource:
                    seeds[idx] = int(seed) + int(mapels[0]) - int(mapels[1])
    print(seeds)
    if zone == 'temp':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            minsource = int(mapels[1])
            maxsource = int(mapels[1]) + int(mapels[2])
            # print(minsource, maxsource, mapels[2])
            for idx, seed in enumerate(seeds):
                # print(seed)
                if int(seed) >= minsource and int(seed) < maxsource:
                    seeds[idx] = int(seed) + int(mapels[0]) - int(mapels[1])
    print(seeds)
    if zone == 'humid':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            minsource = int(mapels[1])
            maxsource = int(mapels[1]) + int(mapels[2])
            # print(minsource, maxsource, mapels[2])
            for idx, seed in enumerate(seeds):
                # print(seed)
                if int(seed) >= minsource and int(seed) < maxsource:
                    seeds[idx] = int(seed) + int(mapels[0]) - int(mapels[1])
    print(seeds)
    if zone == 'loc':
        mapels = row.strip().split(' ')
        if len(mapels) == 3:
            # print(mapels)
            minsource = int(mapels[1])
            maxsource = int(mapels[1]) + int(mapels[2])
            # print(minsource, maxsource, mapels[2])
            for idx, seed in enumerate(seeds):
                # print(seed)
                if int(seed) >= minsource and int(seed) < maxsource:
                    seeds[idx] = int(seed) + int(mapels[0]) - int(mapels[1])


print(seeds)