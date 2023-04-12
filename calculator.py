class calculator():
   def add(a,b):
      return a+b
   def sub(a,b):
      return a-b
   def mul(a,b):
      return a*b
   def div(a,b):
      if a==0:
          print('Division by 0 is Infinity!')
      else:
          return a/b
cal=calculator
x=int(input('Enter the first number : '))
y=int(input('Enter the second number : '))
ch=('1 for addition \2 for substraction \3 for multplication \4 for division')
choice=int(input('Enter your choice : '))
if choice==1:
    print('sum of entered numbers are : ',cal.add(x,y))
elif choice==2:
    print('subraction of entered numbers are : ',cal.sub(x,y))
elif choice==3:
    print('multiplication of entered numbers are : ',cal.mul(x,y))
elif choice==4:
    print('division of entered numbers are : ',cal.div(x,y))
else:
    print('Invalid Entry!! Try Again!!')


