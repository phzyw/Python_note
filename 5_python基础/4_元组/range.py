
# range(start,end,step)
# print(list(range(10)))      # end [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(1,10)))    # start [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(1,10,2)))  # start,end,step [1, 3, 5, 7, 9]

# 水仙花数，三位数，每个位次的3次方的和为它本身
for i in range(100,1000):
    t = str(i)
    a = int(t[2])
    b = int(t[1])
    c = int(t[0])
    if a**3+b**3+c**3 == i:
        print(i)



