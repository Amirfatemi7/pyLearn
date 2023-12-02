import math 


operation = input('''
Please type in the math operation :
+ for addition
- for subtraction
* for multiplication
/ for division
sqrt
sin
cos
tan
cot
fac   
-----------------------
''')


if operation == '+' or operation == '-' or operation == '*' or operation == '/' :
    number_1 = float(input('Enter your first number: '))
    number_2 = float(input('Enter your second number: '))
    if operation == '+':
        print('{} + {} = {}'.format(number_1, number_2,number_1 + number_2))

    elif operation == '-':
        print('{} - {} = {}'.format(number_1, number_2,number_1 - number_2))

    elif operation == '*':
        print('{} * {} = {}'.format(number_1, number_2,number_1 * number_2))

    elif operation == '/':
        print('{} / {} = {}'.format(number_1, number_2,number_1 / number_2))

elif operation == "sqrt" or operation == "sin" or operation == "cos" or operation == "tan" or operation == "cot" or operation == "fac":
    number = float(input('Enter your number: '))
    match operation:
        case "sqrt":
            print(math.sqrt(number))
        case "sin":
            print(math.sin(math.radians(number)))
        case "cos":
            print(math.cos(math.radians(number)))
        case "tan":
            print(math.tan(math.radians(number)))
        case "cot":
            print(math.cot(math.radians(number))) 
        case "tac":
            print(math.factorial(number))

else:
    print('You have not typed a valid operator, please run the program again.')