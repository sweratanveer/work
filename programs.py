# print the integer value
int=23
print(int)

# integer value from the user
int=input("Enter an integer number")
print ("You entered" , int)

# print the character value
char = 'A'
print (char)

# character value from the user
char = input ("Enter a charcater:") [0]
print ("you entered:" , char)

#print the string value
string = "Swera Rana"
print (string)

#string value from user
string = input ("Enter your name :")
print ("you entered:", string)
 
# Write a program to input 2 numbers and print their sum.
first = int(input("Enter 1st number"))
second = int(input ("Enter 2nd number"))
print("sum =" ,first + second) 

# Write a program to input side of a square and print its area.
side= float(input("Enter the side of square"))
print("square=" , side*side)
            
# Write a program to input 2 floating numbers and print their Avearge.
first = float(input("Enter 1st number"))
second = float(input ("Enter 2nd number"))
print("average =" ,first + second/2)

# Write a program to input 2 int numbers(a,b) and print if a is greater than or equal to b if not print false.

a = int(input("Enter 1st number a" ))
b = int(input ("Enter 2nd number b"))
print(a>=b) 

#str1= print('This is a first string')
#str2= print("This is a second string")
#str3= print('''This is a thirs string''')

#str="Swera Rana"
#ch= str[1]
#print(ch)
#print (str [1:4])
str = "i am studying python"
print(str.endswith("on"))
print(str.capitalize())
print(str.replace("m" ,"e"))
print(str.find("s"))
print(str.count("d"))

# Write a program to input user's first name and print it's length.
name = input("Enter your name")
print("length of your name is" , len(name))

# Write a program to find the occurence of $ in string.
str= "I am $ a $ sign and the price of $ sign is 256.00"
print(str.count("$"))

# Write a program to check if a number entered by the user is even or odd.
num= int(input("Enter a number"))
print ("the number is ", num)
if (num%2==0):
    print("The number is even")
else:
    print("The number is odd")

# Write a program to find the greatest of 3 numbers entered by the user.
a=int(input("Enter 1st number a"))
print (a)
b=int(input("Enter second number b"))
print (b)
c=int(input("Enter third number c"))
print (c)
if(a>b & a>c):
    print ("The first number is greater")
elif(b>a & b>c):
    print("The second number is greater")
else:
    print("The third number is greater")

# Write a program if a number is multiple of 7 or not.
x=int(input("Enter a number"))
print(x)
if(x%7==0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")

# Write a program in which we give  coditions to the user firstly user choose a condition and than make a calculator using if else conditions.
print ("Enter 1 for add")
print ("Enter 2 for minus")
print ("Enter 3 for Multiply")
print ("Enter 4 for Divide")
print ("Enter 5 for modulus")
x = int(input("Enter first number x"))
print ("You entered" , x)
y = int(input("Enter second number y "))
print ("You entered" , y)
num = int(input("Enter a number from upper Conditions"))
print ("You entered" , num )
if (num==1):
    print (x+y)
elif (num==2):
    print(x-y)
elif (num==3):
    print (x*y)
elif (num==4):
    print (x/y)
elif (num==5):
    print (x%y)
else:
    print ("Invalid Number")

# Lists in Python
marks=[94.0, 87, 60, 65, 70, 70]
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

student = [ "Swera" , 90, "Lahore"]
print(student[0])
student[0] = "Rana"
print(student) 

# List Slicing
marks=[23, 45, 56, 67]
print(marks)
print(marks[1:4])
print(len(marks))