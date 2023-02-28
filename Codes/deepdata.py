taskDep: list[list[tuple[int, int]]] = [
    [],
    [(0, 100)],
    [(1, 100)],
    [(1, 100)],
    [(1, 100)],
    [(2, 100), (3, 100)],
    [(4, 100)],
    [(5, 100)],
    [(5, 100), (6, 100)],
    [(7, 100), (8, 100)]
]

taskExTime = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

NumberTasks = 10
dataTasks = {0}
actualTasks = [1, 2, 3, 4, 5, 6, 7, 8, 9]
NumberActualTasks = 9

bandwidth = [
    [1000]
]

NumberActualSlots = 2
NumberSlots = 3
actualSlots = [1, 2]

# slot -> datacenter
whichDC = [
    0, 0, 0
]

dataTaskSlot = {
    0: 0
}

