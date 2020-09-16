##Kyler Telge 1825829
print('Birthday Calculator')
print('Current day')
print('Enter current date: (MM/DD/YYYY)')
currentMonth =int(input())
currentDay=int(input())
currentYear=int(input())
print('Enter Birthday: (MM/DD/YYYY)')
birthMonth =int(input())
birthDay =int(input())
birthYear =int(input())
if((currentDay - birthDay) < 0 and (currentMonth - birthMonth)<=0):
    age = (currentYear-birthYear)-1
#else:
 #   age = currentYear-birthYear
print('You are', age, 'years old.')
