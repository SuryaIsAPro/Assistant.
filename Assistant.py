def add(a,b):
 def subract(a,b):
  def multiply(a,b):
   def divide(a,b):

    choice = ('add','subtract','multiply','divide', 'break')


a = int(input('Enter the number:'))
b = int(input('Enter the number:'))

Third = input('Do you want a third value?')
if Third == 'Yes':
    c = int(input('Type the third value:'))


##########################################################
    #Defining all the inputs with 'if' and 'elif' functions.

choice = input('Enter the Function you desire:')

if choice == 'add,add':
  add = a+b+c
  print(add)

elif choice == 'subtract,subtract':
  subtract = a-b-c
  print(subtract)

elif choice == 'multiply,multiply':
  multiply = a*b*c
  print(multiply)


elif choice == 'divide,divide':
    divide = a/b/c
    print(divide)

##################################################################
    #Defining cross operations

elif choice == 'add,subtract':
    addsubtract = a+b-c
    print(addsubtract)

elif choice == 'add,multiply':
    addmultiply = a+b*c
    print(addmultiply)

elif choice == 'add,divide':
    adddivide = a+b/c
    print(adddivide)

##################################################################
     #Defining cross operations

elif choice == 'subtract,add':
    subtractadd = a-b+c
    print(subtractadd)

elif choice == 'subtract,multiply':
    subtractmultiply = a-b*c
    print(subtractmultiply)

elif choice == 'subtract,divide':
    subtractdivide = a+b/c
    print(subtractdivide)

    
#################################################################
     #Defining cross operations
elif choice == 'multiply,add':
    multiplyadd = a*b+c
    print(multiplyadd)

elif choice == 'multiply,subtract':
    multiplysubtract = a*b-c
    print(multiplysubtract)

elif choice == 'multiply,divide':
    multiplydivide = a*b/c
    print(multiplydivide)
#################################################################
     #Defining cross operations
elif choice == 'divide,add':
    divideadd = a/b+c
    print(divideadd)

elif choice == 'divide,subtract':
    dividesubtract = a/b-c
    print(dividesubtract)

elif choice == 'divide,multiply':
    dividemultiply = a/b*c
    print(dividemultiply)

#####################################################################

elif Third == 'No':
    choice = input('Enter the Function you desire:')

   

if choice == 'add':
     add = a+b
     print(add)

elif choice == 'subtract':
  subtract = a-b
  print(subtract)

elif choice == 'multiply':
  multiply = a*b
  print(multiply)


elif choice == 'divide':
  divide = a/b
  print(divide)



###################################################################################################
###################################################################################################


import datetime
dt = datetime.datetime.today()
day = dt.day
month = dt.month
year = dt.year
Time = input('Anything else:')
if Time == 'What is the present day?':
        print(day,month)
elif Time == 'What is the present Month?':
            print(month)
elif Time == 'What is the present year?':
    print(year)

elif Time == 'What is the time now?':
    print(dt)

        




     
