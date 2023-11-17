cost=0
while True:
    age=(input("T="))
    if age=='':
        break
    else:
        age=int(age)
    if age<=2:
        cost=cost+0
    elif age<=12:
        cost=cost+14.00
    elif age>=65:
        cost=cost+18.00
    else:
        cost=cost+23.00
print("The total admission cost for the group is ${:.2f}.".format(cost))



    

