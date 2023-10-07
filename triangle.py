print ("If You Want To Know You can Draw a Triangle With your Numbers :")
num1=int(input('Enter First Side:'))
num2=int(input('Enter Second Side:'))
num3=int(input('Enter Third Side:'))
if num1==0 or num2==0 or num3==0:
    print ('You Can not Draw A Triangle with Zero As a Side')
else:
    if num1<num2+num3 and num2<num1+num3 and num3<num2+num1:
       print ('With This Numbers You Can Draw a Triangle')
    else: print('With This Numbers You Can not Draw a Triangle')

