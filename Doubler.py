class Doubler:
    def __init__(self, n):
        self._n = 2 * n
    def n(self):
        return self._n

if __name__ == '__main__':
    x = Doubler(5)
    assert(x.n() == 10)
    print(x.n())
    y = Doubler(-4)
    assert(y.n() == -8)
    print(y.n())
