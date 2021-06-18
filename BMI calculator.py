weight = float(input("enter your weight in kilograms: "))
height = float(input("enter your height in meters: "))
bmi = weight / height ** 2
if bmi < 18:
    print("you are underweight", "BMI is ", bmi)
elif 18 < bmi < 30:
    print("normal weight", "BMI is ",  bmi)
else: print("you are a fatass", "BMI is ",  bmi)







