# whichTask: dict[str, int] = {
#     'a1': 0, 'a2': 1,
#     'ta1': 2, 'ta2': 3,
#     'b1': 4, 'b2': 5,
#     'tb1': 6, 'tb2': 7,
#     'c1': 8, 'c2': 9,
#     'tc1': 10, 'tc2': 11, 'tc3': 12,
#     'd1': 13, 'd2': 14, 'd3': 15,
#     'td1': 16, 'td2': 17, 'td3': 18, 'td4': 19, 'td5': 20, 
#     'e1': 21, 'e2': 22, 'e3': 23, 'e4': 24,
#     'te1': 25, 'te2': 26, 'te3': 27, 'te4': 28, 'te5': 29, 'te6': 30,
#     'f1': 31, 'f2': 32, 'f3': 33, 'f4': 34, 'f5': 35,
#     'tf1': 36, 'tf2': 37, 'tf3': 38, 'tf4': 39, 'tf5': 40, 'tf6': 41, 'tf4': 42, 'tf5': 43, 'tf6': 44
# }

taskDep: list[list[tuple[int, int]]] = [
    [], [], # a1 a2
    [(0, 150), (1, 180)], # ta1
    [(0, 150), (1, 180)], # ta2
    [], [], # b1, b2
    [(4, 180), (5, 180)], # tb1
    [(4, 180), (5, 180), (6, 100)], # tb2
    [], [], # c1 c2
    [(8, 50), (9, 50)], # tc1
    [(9, 70), (10, 30)], # tc2
    [(8, 30), (10, 20), (11, 20)], #tc3
    [], [], [], # d1 d2 d3
    [(13, 100), (14, 200), (15, 300)], #td1
    [(13, 200), (14, 300), (15, 100)], #td2
    [(14, 50), (16, 200), (17, 200)], #td3
    [(13, 100), (15, 100), (17, 200)], #td4
    [(14, 200), (18, 200)], #td5
    [], [], [], [], #e1-4
    [(21, 60), (22, 80), (23, 120)], #te1
    [(22, 90), (24, 120), (25, 150)], #te2
    [(21, 30), (23, 50), (25, 80)], #te3
    [(22, 160), (26, 100)], #te4
    [(23, 160), (24, 180), (27, 90)], #te5
    [(21, 50), (27, 50), (29, 180)], #te6
    [], [], [], [], [], #f1-5
    [(31, 300)], #tf1
    [(32, 100), (36, 100)], #tf2
    [(33, 200), (36, 120)], #tf3
    [(34, 100), (36, 100)], #tf4
    [(31, 50), (32, 50), (33, 50), (37, 100), (38, 150)], #tf5
    [(31, 70), (34, 70), (39, 90)], #tf6
    [(33, 100), (35, 200), (40, 300)], #tf7
    [(32, 150), (35, 100), (40, 500), (41, 50)], #tf8
    [(31, 250), (33, 30), (34, 80), (35, 200), (42, 200), (43, 200)] #tf9
]

taskExTime = [0, 0, 1.5, 1.5, 0, 0, 2.5, 1, 0, 0, 4, 1, 2, 0, 0, 0, 2, 2, 1.5, 1, 1, 0, 0, 0, 0, 4, 2, 3, 2, 1, 3, 0, 0, 0, 0, 0, 4, 2, 1, 3, 1, 1.5, 2.5, 2, 3.5]

NumberTasks = 45
dataTasks = {0, 1, 4, 5, 8, 9, 13, 14, 15, 21, 22, 23, 24, 31, 32, 33, 34, 35}
actualTasks = [2, 3, 6, 7, 10, 11, 12, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 36, 37, 38, 39, 40, 41, 42, 43, 44]
NumberActualTasks = 27

bandwidth = [
    [1200, 80, 150, 0, 0, 0, 0, 0, 0, 0, 0, 500, 0],
    [100, 1200, 120, 160, 200, 0, 0, 0, 0, 0, 0, 0, 0],
    [80, 100, 1200, 200, 50, 0, 0, 300, 0, 0, 400, 0, 0],
    [0, 150, 180, 1200, 20, 120, 0, 0, 200, 0, 0, 0, 0],
    [0, 200, 40, 20, 1200, 150, 200, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 250, 180, 1200, 0, 90, 0, 0, 50, 0, 500],
    [0, 0, 0, 0, 200, 0, 1200, 0, 0, 70, 40, 0, 0],
    [0, 0, 300, 0, 0, 60, 0, 1200, 20, 90, 0, 0, 0],
    [0, 0, 0, 300, 0, 0, 0, 30, 1200, 0, 90, 500, 0],
    [0, 0, 0, 0, 0, 0, 70, 50, 0, 1200, 0, 0, 0],
    [0, 0, 400, 0, 0, 40, 60, 0, 50, 0, 1200, 0, 0],
    [500, 0, 0, 0, 0, 0, 0, 0, 400, 0, 0, 1200, 500],
    [0, 0, 0, 0, 0, 400, 0, 0, 0, 0, 0, 500, 1200]
]

NumberActualSlots = 31
NumberSlots = 31 + 13
actualSlots = [1, 2, 4, 6, 7, 8, 10, 11, 13, 15, 16, 17, 18, 19, 21, 22, 24, 25, 27, 28, 30, 32, 33, 35, 36, 37, 38, 40, 41, 42, 43]

# slot -> datacenter
whichDC = [
    0, 0, 0, #0
    1, 1, #3
    2, 2, 2, 2, #5
    3, 3, 3, #9
    4, 4, #12
    5, 5, 5, 5, 5, 5, #14
    6, 6, 6, #20
    7, 7, 7, #23
    8, 8, 8, #26
    9, 9, #29
    10, 10, 10, #31
    11, 11, 11, 11, 11, #34
    12, 12, 12, 12, 12 #39
]

dataTaskSlot = {
    0: 0,
    1: 9,
    4: 0,
    5: 5,
    8: 3,
    9: 14,
    13: 12,
    14: 20,
    15: 26,
    21: 9,
    22: 14,
    23: 23,
    24: 31,
    31: 26,
    32: 39,
    33: 29,
    34: 34,
    35: 39
}


