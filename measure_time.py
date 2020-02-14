from functools import wraps
from time import time

def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            # print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
            print("Total execution time: {timed} ms".format(timed = end_ if end_ > 0 else 0))
    return _time_it


@measure
def your_fucnction_here():
  total = 0
  for i in range(0,1000000):
    total += i
  return total

your_function_here()
