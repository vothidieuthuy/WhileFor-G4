n=int(input('n='))
if n==0:
    print('Error')
else:
    i=0
    S=0
    while n!=0:
        S=S+n
        i=i+1
        n=int(input('n='))
    Average=S/i
    print('The average is:',Average)
        


