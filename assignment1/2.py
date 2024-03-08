
side1 = float(input('Enter first side: '))
side2 = float(input('Enter second side: '))
side3 = float(input('Enter third side: '))

if side1 > side2 + side3:
    print(" u cant draw this triangle ")
elif side2 > side1 + side3:
    print(" u cant draw this triangle ")
elif side3 > side1 + side2:
    print(" u cant draw this triangle ")
else:
    print("* u can draw it*")