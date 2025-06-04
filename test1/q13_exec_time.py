#Q13. Create a class Timer using __enter__ and __exit__ dunder methods to measure execution time of a code block.
import time
class timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self,exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.duration = self.end - self.start
        print(f'time: {self.duration} seconds')

with timer():
    total = 0
    for i in range(1, 1000000):
        total += i