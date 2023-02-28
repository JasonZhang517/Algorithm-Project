import matplotlib.pyplot as plt

INFINITY = 20.0

with open('curve.txt', 'r') as f:
    x = []
    y = []
    cx = []
    ymin = []
    ymax = []
    n = 0
    for line in f.readlines():
        words = line.split()
        n += 1
        ys = list(map(lambda w: INFINITY if w == 'inf' else float(w), words))
        x += [n] * len(ys)
        y += ys
        cx.append(n)
        ymin.append(min(ys))
        ymax.append(max(ys))

    plt.plot(cx, ymin, 'r')
    plt.plot(cx, ymax, 'y')
    plt.scatter(x, y, s = 0.5)
    plt.xlabel('Iteration')
    plt.ylabel('Time')
    plt.legend(['Minimum time', 'Maximum time', 'All times'])
    plt.savefig('plot.png')
