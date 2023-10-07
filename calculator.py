import math
print('Welcome to My Calculator, Please Enter:')
print('+ , - , * , / , sin , cos , tan , cot , sqrt , fact')
op = input('For the Operand You Want: ')
if op=='+' or op=='-' or op=='*' or op=='/' :
    num1= float(input('Please Enter Your First Number: '))
    num2= float(input('Please Enter Your Second Number: '))
elif op=='sin' or op=='cos' or op=='tan' or op=='cot' or op=='sqrt':
    num1=float(input('Please Enter Your Number: '))
elif op=='fact':
    num3 = int(input('Please Enter an Integer Number: '))
else: print('Sorry, Your Choice is not in the Operands Of Calculator')

if op=='+':
    print(num1,'+',num2,'= ',num1+num2)
elif op=='-':
    print(num1,'-',num2,'=',num1-num2)
elif op=='*':
    print(num1,'*',num2,'=',num1*num2)
elif op=='/':
    if num2==0 :
        print('OverFlow')
    else:
        print(num1,'/',num2,'=',num1/num2)
elif op=='sin':
    print('sin(',num1,')=',math.sin(num1))
elif op=='cos':
    print('cos(',num1,')=',math.cos(num1))
elif op=='tan':
    print('tan(',num1,')=',math.tan(num1))
elif op=='cot':
    print('cot(',num1,')=', 1/math.tan(num1))
elif op=='sqrt':
    print('sqrt(',num1,')=',math.sqrt(num1))
elif op=='fact':
    print('fact(',num3,')=',math.factorial(num3))
