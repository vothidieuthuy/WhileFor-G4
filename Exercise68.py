while True:
    bits=input("")
    if bits=='':
        break
    elif len(bits)!=8:
        print("Error")
        continue
    else:
        ones_count=0
        for bit in bits:
            if bit=='1':
                ones_count+=1
    if ones_count%2==0:
        parity_bit='0'
    else:
        parity_bit='1'
    print("Parity bit:", parity_bit)
    