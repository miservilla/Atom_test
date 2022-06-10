import re
import time

def sumk(k):
    start = time.time()

    total = 0
    for i in range(k + 1):
        total = total + i
    end = time.time()

    return total, end-start

for i in range(5):
    print("Sum: %d, time taken: %f" % sumk(10000))
