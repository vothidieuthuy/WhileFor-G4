pi = 3
for i in range(1, 16):
    if i % 2 == 0:
        pi -= 4 / ((2 * i + 1) * (2 * i + 2) * (2 * i + 3))
    else:
        pi += 4 / ((2 * i + 1) * (2 * i + 2) * (2 * i + 3))
    print(pi)