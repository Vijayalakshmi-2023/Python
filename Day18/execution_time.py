import functools
import time
import datetime

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print(f"[{datetime.datetime.now()}] Starting '{func.__name__}'...")
        
        result = func(*args, **kwargs)
        
        end = time.perf_counter()
        duration = end - start
        print(f"[{datetime.datetime.now()}] Finished '{func.__name__}' in {duration:.4f} seconds")
        print("-" * 50)
        return result
    return wrapper
@timeit
def process_large_list():
    return sum([i**2 for i in range(1_000_000)])

@timeit
def simulate_wait():
    time.sleep(2)
    return "Done sleeping"
process_large_list()
simulate_wait()
