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

def timetrials(func, k, trials = 10):
    totaltime = 0
    for i in range(trials):
        totaltime += func(k)[1]
    print("average =%10.7f for k = %d" % (totaltime / trials, k))

timetrials(sumk, 10000)
timetrials(sumk, 100000)
timetrials(sumk, 1000000)
timetrials(sumk, 10000000)

def sumk2(k):
    start = time.time()
    total = (k * (k + 1) // 2) #// is floor or 'integer' division
    end = time.time()
    return total, end - start

print()
timetrials(sumk2, 10000)
timetrials(sumk2, 100000)
timetrials(sumk2, 1000000)
timetrials(sumk2, 10000000)
timetrials(sumk2, 100000000)
