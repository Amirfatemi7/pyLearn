import random

n = int(input("number of array len : "))

array = random.sample(range(n),n)
# for i in range(n):
#     array.append(random.sample(range(n),1))


print(array)