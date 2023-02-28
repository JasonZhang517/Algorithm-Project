import random as rd
import math
from scheduler_ngreedy import *

N = NumberActualTasks
M = NumberActualSlots

def fairDispatch(n, m):
    f = math.floor(n / m)
    c = math.ceil(n / m)
    cn = n - m * f
    fn = m - cn
    return (f, fn, c, cn)

class Ind:
    def __init__(self, permT, permN):
        self.permT = permT.copy()
        self.permN = permN.copy()
        sc = Scheduler(permT, permN)
        self.cost = sc.cost
        
    def __lt__(self, other):
        return self.cost < other.cost

def permCrossOver(p1, p2, prob):
    if rd.random() >= prob:
        return
    
    s = len(p1)
    l = rd.randint(0, s)
    h = rd.randint(0, s)
    l, h = min(l, h), max(l, h)
    tmp1 = p1.copy()
    tmp2 = p2.copy()
    set1 = set(p1[l: h])
    set2 = set(p2[l: h])
    k = 0
    for i in range(s):
        if not tmp2[i] in set1:
            if (k == l):
                k = h
            p1[k] = tmp2[i]
            k += 1
    k = 0
    for i in range(s):
        if not tmp1[i] in set2:
            if (k == l):
                k = h
            p2[k] = tmp1[i]
            k += 1

def permMutation(p, prob):
    for i in range(len(p) - 1):
        if rd.random() < prob:
            tmp = p[i]
            p[i] = p[i + 1]
            p[i + 1] = tmp

class Population:
    def __init__(self, size, cp, mp):
        self.cp = cp
        self.mp = mp
        self.size = size
        self.nowGen = []
        self.firstGen()
    
    def firstGen(self):
        permT = list(map(lambda i: actualTasks[i], range(N)))
        f, fn, c, cn = fairDispatch(N, M)
        permN = ([f] * fn) + ([c] * cn)
        for _ in range(self.size):
            rd.shuffle(permT)
            rd.shuffle(permN)
            self.nowGen.append(Ind(permT, permN))

    def nextGen(self):
        rd.shuffle(self.nowGen)
        for i in range(0, self.size - 1, 2):
            chT1 = self.nowGen[i].permT
            chT2 = self.nowGen[i + 1].permT
            chN1 = self.nowGen[i].permN
            chN2 = self.nowGen[i + 1].permN
            
            permCrossOver(chT1, chT2, self.cp)
            permMutation(chT1, self.mp)
            permMutation(chT2, self.mp)

            if rd.random() < self.mp:
                rd.shuffle(chN1)

            if rd.random() < self.mp:
                rd.shuffle(chN2)

            self.nowGen.append(Ind(chT1, chN1))
            self.nowGen.append(Ind(chT2, chN2))
        
        self.nowGen.sort()
        while len(self.nowGen) > self.size:
            self.nowGen.pop()

if __name__ == '__main__':
    output = open('curve.txt', 'w')
    initBand()
    initTopo()
    p = Population(256, 0.7, 0.05)
    ITER = 128
    for _ in range(ITER):
        p.nextGen()
        line = ''
        for ind in p.nowGen:
            line += f'{ind.cost} '
        line += '\n'
        # print(line[:10], end = '')
        output.write(line)
    
    print(p.nowGen[0].cost)
