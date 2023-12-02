print("------------------------------------------")

weight = float(input('write your weight (kg):'))
height = float(input('write your height (m):'))


bmi = weight/(height**2)

if bmi < 18.5:
    print("Your BMI is : {}. you are under weight.".format(bmi))
elif bmi >= 18.5 and bmi <25:
    print("Your BMI is : {}. you are normal weight.".format(bmi))
elif bmi >= 25 and bmi <30:
    print("Your BMI is : {}. you are over weight.".format(bmi))
elif bmi >= 30 and bmi <35:
    print("Your BMI is : {}. you are obesity.".format(bmi))
elif bmi >= 35 and bmi <40:
    print("Your BMI is : {}. you are extreme obesity.".format(bmi))
