
n = int(input("write n "))

countor = 1
fn_1 = 0
fn_2 = 1
number = 0

while countor <= n:
    fn_1 , fn_2 = fn_2 , number
    number = fn_1 + fn_2
    countor +=1
    print(number," ")