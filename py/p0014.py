from multiprocessing import Process, Manager
from random import random as rand
from time import perf_counter_ns


def worker(pnum, returns, limit):
    circles = 0
    for _ in range(limit):
        circles += rand()**2 + rand()**2 < 1
    returns[pnum] = (circles, limit)


if __name__ == '__main__':
    print('Output stability test (Ctrl + C to stop)')
    manager = Manager()
    out = []
    for _ in range(100):
        start = perf_counter_ns()
        returns = manager.dict()
        workers = []
        for i in range(100):
            w = Process(target=worker, args=(i, returns, int(5e5)))
            workers.append(w)
            w.start()
        for w in workers:
            w.join()
        circles = iterations = 0
        for c, i in returns.values():
            circles += c
            iterations += i
        est = circles / iterations * 4 * 1000 // 1 / 1000
        out.append(est)
        elapsed = perf_counter_ns() - start
        print(f'Test #{len(out)}: {out[-1]}, took {elapsed // 1e6:,.0f}ms for {iterations:,} iterations '
              f'(Accuracy: {sum(str(n) == "3.141" for n in out) * 100 / len(out):.02f}%)')
    print(f'Overall Accuracy: {sum(str(n) == "3.141" for n in out) * 100 / len(out):.02f}%')
