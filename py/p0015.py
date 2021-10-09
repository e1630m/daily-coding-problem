from random import randint


def random_pick(stream, interval=10):
    i = 0
    while True:
        yield stream[randint(i, i + interval - 1)]
        i += interval


def random_pick_two(stream):
    i = 0
    while True:
        if randint(1, i + 1) == 1: 
            yield stream[i]
        i += 1

num_picks = {i: 0 for i in range(10)}
# for i in random_pick(range(int(1e50))):
for i in random_pick_two(range(int(1e50))):
    num_picks[i % 10] += 1
    print(num_picks)
