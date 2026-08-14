
# 'Day 2: 30 Days of python programming'
import math
import keyword
first_name = 'Aqila'
last_name = 'Nasiry'
full_name = 'Aqila Nasiry'
country = 'USA'
city = 'Sacramento'
age = 25
year = 2026
is_married = True
is_true = 'Student'
fav_color , first_school_friend, fav_food = 'Pink' , 'Farkhunda', 'Pizza'


#Level2 
print('Type of first name is: ' , type(first_name))
print('Type of last name is: ' , type(last_name))
print('Type of age is: ' , type(age))
print('Type of is_married is: ' , type(is_married))
print('Type of is_true is: ' , type(is_true))
print('Type of fav_color is: ' , type(fav_color))


print('Length of first_name is: ' , len(first_name))
print('Length of last_name is: ' , len(last_name))

if first_name > last_name:
    print('First name is longer than last name')
elif last_name > first_name:
    print('Last name is longer than first name')
else:
    print('First and last names are equal.')

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
#exp = pow(num_one , num_two)
floor_division = num_one // num_two

radius = 30
#A = pi (r to the pow of 2)
area_of_circle = math.pi * (radius ** 2)

#C = 2 * pi * r
circum_of_circle = 2 * math.pi * radius

print('Area of circle :' , area_of_circle)
print('Circumference of circle: ' , circum_of_circle)





user_radius = int(input('Enter radius: '))
user_area = math.pi * (user_radius ** 2)

print(f'Area of circle with radius {user_radius}: {user_area:.2f}')


first_name = input('Enter your first name: ')

last_name = input('Enter your last name: ')

country = input('Enter your country: ')

age = int(input('Enter your age: '))

print('PROFILE DISPLAY:')
print(f'First Name: {first_name} {last_name}')
print(f'Country: {country}')
print(f'Age: {age}')
print(keyword.kwlist)
