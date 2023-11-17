import random
total_flips = 0
for i in range (10):
    flips = 0
    H = 0
    T = 0
    while True:
        result = random.choice(['H', 'T'])  
        print(result, end=' ')
        flips += 1
        if result == 'H':
            H += 1
            T = 0
        else:
            T += 1
            H = 0
        if H == 3 or T == 3:
            break
    print('(',flips,' flips',')', sep='')
    total_flips += flips
average_flips_needed = total_flips / 10
print('On average,',average_flips_needed,'flips were needed')
