from threading import Thread 
from time import sleep, perf_counter_ns


class Scheduler():
    def __init__(self):
        self.queue = []
        self.run = True
        self.thread = Thread(target=self.scheduler)
        self.thread.start()

    def add_queue(self, func, ms):
        launch_after = ms * int(1e6) + perf_counter_ns()
        self.queue.append((func, launch_after))
         
    def terminate(self):
        self.run = False
        self.thread.join()

    def scheduler(self):
        while self.run:
            sleep(0.00001)
            now = perf_counter_ns()
            for i, (func, limit) in enumerate(self.queue):
                if now > limit:
                    func()
            self.queue = [(func, limit) for func, limit in self.queue if now <= limit] 


def target():
    print('target is running')


s = perf_counter_ns()
a = Scheduler()
a.add_queue(target, 5)
sleep(2)
a.add_queue(target, 5)
sleep(1)
a.terminate()
