pennies_niken = 5
niken = 0.05
total=0.00
price=input('Enter the price:')
while price != '':
    total = total + float(price)
    price=input("Enter the price:")
print('Total cost of all items: %.02f' % total)
remainder = total * 100 % pennies_niken
if remainder < 2.5:
    amount_due = total - remainder / 100
else:
    amount_due = total + niken - remainder / 100
print('Amount due if paying with cash %.02f' % amount_due)

