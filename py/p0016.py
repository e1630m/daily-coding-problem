class Log():
    def __init__(self, n):
        self.log = []
        self.cur = 0
        self.n = n

    def record(self, order_id):
        if len(self.log) < self.n:
            self.log.append(order_id)
        else:
            self.log[self.cur] = order_id
        self.cur += 1
        self.cur %= self.n

    def get_last(self, i):
        return self.log[self.cur - i]
