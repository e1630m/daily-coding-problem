def rooms(intervals):
    num_rooms = 0
    for i in range((length := len(intervals) - 1)):
        overlap = 0
        for j in range(i + 1, length + 1):
            s, e = intervals[i]
            sj, ej = intervals[j]
            overlap += not (s > ej or e < sj)
        num_rooms = max(num_rooms, overlap)
    return num_rooms


test = [(30, 75), (0, 50), (60, 150)]
print(f'rooms({test}): {rooms(test)}')
