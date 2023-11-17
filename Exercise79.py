import random
max_num = 0
up_count = 0
for i in range(1,100):
  num = random.randint(1, 100)
  if num > max_num:
    max_num = num
    up_count += 1
  if num == max_num:
    print(num, "<== Update")
  else:
    print(num)

print("The maximum value found was", max_num)
print("The nmaximum value was updated", up_count, "times")
