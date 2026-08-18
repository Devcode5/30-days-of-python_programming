
import math
print('Addition:' , 1+2)
print('Division' , 4/2)
print('Division' , 7/2)
print('Division' , 7//2)

print('FLoating point number, PI' , 3.14)
print('Multiplying complex numbers' , (1+1j) * (1-1j))

# Area of a Circle
radius = 10 
area_of_circle = 3.14 * radius **2
print( 'Area of a Circle: ',  area_of_circle)

#Area of a Rectangle.  A = W*I
length = 10
width = 20
area_of_rectangle = length * width
print('Area of a Rectangle: ' , area_of_rectangle)

# Weight of an object.  W = m * g
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight , 'N')


#Density of liquid. D = m/v

mass = 75
volumue =  0.075
density = mass / volumue
print(density , 'kg/m^3')

#Comparison Operators
print(3>2)
print(3<2)

print(2<=1)
print(3!=3)
print(len('mango') == len('avocado'))
print(len('milk') <= len('water'))
print('True == True: ' , True == True)
print('True == False: ' , True == False)
print('False == False:' , False == False)

# is - is not - in - not in
print('1 is 1' , 1 is 1)
print('1 is not 2' , 1 is not 2)
print('A in Aqila' , 'A' in 'Aqila')
print('Coding' in 'Coding for all')
print('B not in Aqila' , 'B' not in 'Aqila')

#Logical Operators
print('Logical Operators')
print(3>2 and 2<4)
print(3>2 or 3<3)
print(not 3>2)
print(not True)
print(not not True)
print(not(3>2 and 4<8))

#Excercise Day 3
age = 20
height = 3.7
comp_number = 1+1j

# 1# #area = 0.5 * b * h
base = float(input('Enter base: '))
height = float(input('Enter height: '))
area = int( 0.5 * base * height)
print('The area of triangle is ' , area)


# 2#perimeter of triangle: perimeter = a + b + c
a= float(input('Enter side a: '))
b = float( input('Enter side b: '))
c = float(input('Enter side c: '))
perimeter = int(a + b + c)
print('The perimeter of the triangle is ' , perimeter)


#6
###################################################################################
length = float(input('Enter length: '))
width = float(input('Enter width: '))
#area = length * width
#perimeter = 2*(length + width)
area =  int(length * width)
perimeter = int(2 * (length * width))
print('Area and perimeter are as follows: ' , area , 'and' , perimeter)
##################################################################################
#8 - Slope , x-intercept , y-intercept of y=2x-2 , Formula: y=mx-b
m = 2
b = -2

x_intercept  = -b/m
y_intercept = b

print(f'Y-intercept: (0,{y_intercept})')
print(f'X-intercept: ({x_intercept} , 0)')


###################################################################################
#9 slope is (m= y2-y1/x2-x1) -> slope? Euclidean distance between (2,2) and (6,10)

m = y2-y1 / x2-x1
x1 , y1 = 2 , 2
x2 , y2 = 6 , 10
slope = (y2-y1) / (x2-x1)
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f'Slope (m): {slope}')
print(f'fEuclidean Distance:{distance:.2f}')
###################################################################################
#10 Comparing slopes from task 8 and 9
slope1 = 2
slope2 = 2.0

print(f'Slope 1: {slope1}')
print(f'Slope2: {slope2}')

print('Are slopes equal?' , slope1 == slope2)
print('Is Slope1 greater than slope2?' , slope1 > slope2)
print('Is Slope1 less than slope2?' , slope1 < slope2)


###################################################################################
#11. y = x^2 +6x +9
x = 0
y = x**2  + 6*x + 9
print(f'Y value at x=0 is: {y}')

x = 1
y = x**2  + 6*x + 9
print(f'Y value at x=1 is: {y}')

x = 2
y = x**2  + 6*x + 9
print(f'Y value at x=2 is: {y}')

x = -3
y = x**2 + 6*x +9
print(f'Y value at x=-3 is: {y}')



#12
len_python = len('python')
len_dragon = len('dragon')
is_not_equal = len('python') != len('dragon')

print(f'Comparison(len("python") != len("dragon")): {is_not_equal}')

###################################################################################
#13


result = ('on' in 'python') and ('on' in 'dragon')
print(result)

sentence = 'I hope this course is not full of jargon'
print('jargon' in sentence)

#16
len_python = str(float(len('python')))
print(len_python)
print(type(len_python))

###################################################################################
#17 checking if number is even or not
number = 10
remainder = number %2
print(remainder)

is_even = (remainder == 0)
print(is_even)

number = int(input('Enter a number: '))

if number %2 ==0:
    print(f'{number} is an even number')
else:
    print(f'{number} is an odd number')

###################################################################################
#18
floor_div = 7//3
int_val = int(2.7)
print(floor_div == int_val)

num1 = int(float('9.8'))
num2 = 10
print(type(num1) == type(num2))

###################################################################################
#21 - Calculate pay of the person
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
pay_of_the_person = hours * rate_per_hour
print(f'Your weekly earning is {pay_of_the_person}')

###################################################################################
#22 calculate number of seconds a person can live
years= int(input('Enter number of years you have lived: '))
seconds_in_1year = 31536000
total_seconds= years * seconds_in_1year
print(f'You have lived {total_seconds}' )


###################################################################################
#23 - display table

for i in range(1,6):
    print(f"{i} {i**0} {i**1} {i**2} {i**3}")
