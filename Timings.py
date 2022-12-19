import time

class Timer:
    def __init__(self, interval):
        self.interval = interval
        self.time_set = time.time()
        self.time_since = 0

    def update(self):
        self.time_since = time.time() - self.time_set