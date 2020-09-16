print('Birthday Calculator')
print('Current day')
print('Enter current date: (MM/DD/YYYY)')
currentMonth =int(input())
currentDay=int(input())
currentYear=int(input())
print('Birthday')
birthMonth =int(input())
birthDay =int(input())
birthYear =int(input())
age = currentYear - birthYear
if(birthMonth>=currentMonth and currentDay>birthDay):
    age = currentYear - birthYear
print('You are', age, 'years old.')
