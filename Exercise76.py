n = int(input("Enter an integer (2 or greater): "))
factor = 2
if n < 2:
        print("Error: Invalid number")
else:
    while factor <= n:
        if n % factor == 0:
            n = n // factor 
            print(factor)
        else:
            factor = factor + 1
        

       




