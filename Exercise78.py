q = int(input("Enter a decimal number: "))
result = ""
while q > 0:
    r = q % 2
    result = str(r) + result
    q //= 2
        
print("The binary representation is", result)
