import math

def P(n,k):
    return number_artifact(n).factorial().divide(number_artifact(n-k).factorial())

def C(n,k):

    return P(n,k).divide(number_artifact(k).factorial())

class number_artifact():
    def __init__(self,n):
        self.factors = {}
        self.define(n)

    def compute(self):
        num = 1
        for f in self.factors.keys():
            num *= math.pow(f, self.factors[f])
        return int(num)

    def factorial(self):
        for i in range(2, int(self.compute())):
            na = number_artifact(i)
            self.multiply(na)
        return self

    def compute_combinatorics(self, n, k, sd=False, cd=False, multi=False):
        if not multi:
            if sd and cd:
                return P(n,k)
            if sd and not cd:
                return C(n,k)
            if not sd and cd:
                return C(n+k-1, k)
            if not sd and not cd:
                return 1

    def define(self,n):
        self.factors = self.get_prime_factors(n)

    def get_prime_factors(self, n):
        dd = {}
        if n > 1:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    if i not in dd.keys():
                        dd[int(i)] = 0
                    dd[int(i)] += 1
                    n /= i
                    i = 2
                else:
                    i += 1
            if n not in dd.keys():
                dd[int(n)] = 0
            dd[int(n)] += 1
        return dd



    def divide(self, n):
        for i, factor in enumerate(n.factors.keys()):
            self.factors[factor] -= n.factors[factor]

        return self

    def multiply(self, n):
        for i, factor in enumerate(n.factors.keys()):
            if factor not in self.factors.keys():
                self.factors[factor] = 0
            self.factors[factor] += n.factors[factor]

        return self

    def show(self):
        print(self.factors)

def factor(n):
    k= 1
    for i in range(2,n+1):
        k *= i
    return k

def compute_faster(n,k):
    return int(int(factor(n))/int((factor(n-k)*factor(k))))

import time
start = time.time()
print(C(10000,50).compute())
n = time.time() - start
start = time.time()
print(n)
print(compute_faster(10000,50))
print(time.time()-start)
