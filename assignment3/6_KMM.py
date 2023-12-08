# first = int(input('first:'))
# second = int(input('second:'))
 
# if first > second:
#   first, second = second, first
# for i in range(1,first+1):
#   if first%i == 0 and second%i == 0:
#     gcd = i

# lcm = (first*second)/gcd

first = int(input('first:'))
second = int(input('second:'))
 
for i in range(1,second+1):
    if first % i == 0 and second % i == 0:
        bmm = i
print(first * second / bmm)