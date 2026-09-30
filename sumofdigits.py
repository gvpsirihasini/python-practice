n=int(input('enter the digit:'))
s=0
r=0
while n>0:
  r=n%10
  s=s+r
  n=n//10
print('sum of the digits is',s)
