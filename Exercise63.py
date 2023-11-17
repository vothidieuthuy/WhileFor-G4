print("{:<15} {:<15}".format("Celsius", "Fahrenheit"))
for C in range(0, 101, 10):
    F = (C * 9/5) + 32
    print("{:<15} {:<15}".format(C, F))