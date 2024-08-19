import random

from my_package import my_math

# a = my_math.fun(4,5)
# print(a)

list1 = [1,2,4,5,6,'23']
total = 0
for i in range(len(list1)):
    total += int(list1[i])
print(total)

list2 = ''
for j in range(len(list1)):
    list2 += str(list1[j])
print(list2)