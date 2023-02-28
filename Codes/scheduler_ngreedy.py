from toydata import *

INFINITY = float('inf')

import heapq as pq
from collections import deque

band = bandwidth.copy()

def initBand():
    l = len(bandwidth)
    for k in range(l):
        for i in range(l):
            for j in range(l):
                band[i][j] = max(band[i][j], min(band[i][k], band[k][j]))

def initTopo():
    pass

class Task:
    def __init__(self, tid, sid, finishT):
        self.tid = tid
        self.sid = sid
        self.finishT = finishT
    def __lt__(self, other):
        return self.finishT < other.finishT

class Scheduler:
    def __init__(self, permT, permN):
        self.permT = permT
        self.permN = permN
        self.cost = self.schedule()
        
    def schedule(self):
        whichSlot = dataTaskSlot.copy()
        timeNow = 0.0
        exeQue = [deque() for _ in range(NumberActualSlots)]

        k = 0
        for i in range(NumberActualSlots):
            for _ in range(self.permN[i]):
                exeQue[i].append(self.permT[k])
                whichSlot[self.permT[k]] = actualSlots[i]
                k += 1

        executing = [False] * NumberActualSlots
        completed = dataTasks.copy()
        toFinish = []

        while True:
            for i in range(NumberActualSlots):
                if executing[i] or len(exeQue[i]) == 0:
                    continue
                todo = exeQue[i][0]
                canDo = True
                doTime = 0.0
                for dep, amount in taskDep[todo]:
                    if dep in completed:
                        src = whichDC[whichSlot[dep]]
                        dst = whichDC[whichSlot[todo]]
                        if band[src][dst] == 0:
                            doTime = INFINITY
                        else:
                            doTime = max(doTime, taskExTime[todo] + amount / band[src][dst])
                    else:
                        canDo = False
                        break
                if canDo:
                    pq.heappush(toFinish, Task(todo, i, timeNow + doTime))
                    exeQue[i].popleft()
                executing[i] = canDo
            if len(toFinish) == 0:
                if all(map(lambda q: len(q) == 0, exeQue)):
                    return timeNow
                else:
                    return INFINITY
            now = pq.heappop(toFinish)
            completed.add(now.tid)
            executing[now.sid] = False
            timeNow = now.finishT
            


