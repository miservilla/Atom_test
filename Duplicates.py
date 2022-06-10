import time

def duplicates1(L):
    n = len(L)
    for i in range(n):
        for j in range(n):
            if i !=j and L[i] == L[j]:
                return True
    return False

assert(duplicates1([1, 2, 6, 3, 4, 5, 6, 7, 8]))
assert(not duplicates1([1, 2, 3, 4]))

def duplicates2(L):
    n = len(L)
    for i in range(1, n):
        for j in range (i):
            if L[i] == L[j]:
                return True
    return False

def duplicates3(L):
    n = len(L)
    return any(L[i] == L[j] for i in range(1, n) for j in range(i))

def duplicates4(L):
    n = len(L)
    L.sort()
    for i in range(n - 1):
        if L[i] == L[i + 1]:
            return True
    return False

def duplicates5(L):
    n = len(L)
    L.sort()
    return any(L[i] == L[i + 1] for i in range(n - 1))

def duplicates6(L):
    s = set()
    for e in L:
        if e in s:
            return True
        s.add(e)
    return False

def duplicates7(L):
    return len(L) != len(set(L))

def duplicates8(L):
    s = set()
    return any(e in s or s.add(e) for e in L)

n = 1000

for i in range(5):
    start = time.time()
    duplicates1(list(range(n)))
    timetaken = time.time() - start
    print("Time taken for n = ", n, ": ", timetaken)

def timetrials(func, n, trials = 10):
    totaltime = 0
    for i in range(trials):
        start = time.time()
        func(list(range(n)))
        totaltime += time.time() - start
    print("average =%10.7f for n = %d" % (totaltime/trials, n))

for n in [50, 100, 200, 400, 800, 1600, 3200]:
    print("Quadratic: ", end="")
    timetrials(duplicates3, n)
    print("Sorting:", end="")
    timetrials(duplicates5, n)
    print("Sets:", end="")
    timetrials(duplicates7, n)
    print("---------------------------")

# for n in [50, 100, 200, 400, 800, 1600, 3200]:
#    timetrials(duplicates8, n)
