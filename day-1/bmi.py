#body mass index calculator

import math

weight = input('How is your weight? (in kilograms): ')
tall = input('How tall are you? (in meters): ')

bmi = math.floor(float(weight) / pow(float(tall), 2))

print('your bmi is ' + str(bmi))
if bmi < 18:
    print('You are underweight')
elif bmi > 18 and bmi <= 24.9:
    print('Your weight is normal')
elif bmi >= 25 and bmi <= 29.9:
    print('You are overweight') 
elif bmi >= 30 and bmi <= 34.9:
    print('You are obese')
else:
    print('You are extremely obese')