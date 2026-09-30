num1=int(input('enter num1:'))
num2=int(input('enter num1:'))
if (num1>num2):
  dividend=num1
  divisor=num2
else:
  dividend=num2
  divisor=num1
while (remainder!=0):
  remainder=dividend%divisor
  dividend=divisor
  divisor=remainder
  
