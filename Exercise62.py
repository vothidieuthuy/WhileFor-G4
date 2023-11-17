print("{:<15} {:<15} {}".format("Original price", "Discount amount", "New price"))
or_price = [4.95, 9.95, 14.95, 19.95, 24.95]
sale=60
for i in or_price:
    dis_amount=i*(60/100)
    new_price=i-dis_amount
    print("${:<14.2f} ${:<14.2f} ${:<.2f}".format(i,dis_amount,new_price))


    

    