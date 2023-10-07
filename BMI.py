from emoji import emojize
print('This is a Test for Calculating Your Body Mass Index' )
w=float(input('Please Enter Your Weight In KG :'))
h=float(input('Please Enter Your Height In CM :'))
BMI=w/((h/100)**2)
print('Your Body Mass Index:',BMI)
if (BMI < 18.5) :
    print ('Underweight',emojize(":anxious_face_with_sweat:"))

elif (18.5 <= BMI <= 24.9) :
    print ('Normal Weight',emojize(":beaming_face_with_smiling_eyes:"))

elif (25 <= BMI <= 29.9):
    print ('Overweight',emojize(":expressionless_face:"))

elif (30 <= BMI <= 34.9):
    print ('Obesity',emojize(":face_with_crossed-out_eyes:"))

elif (35 <= BMI <= 39.9):
    print ('Extreme Obesity',emojize(":enraged_face:"))