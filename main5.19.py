##Kyler Telge 1825829
autoshop = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12, "-":"No service"}
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
total=0
print()
print('Select first service:')
first_choice = input()
print('Select second service:\n')
second_choice = input()
print('Davy\'s auto shop invoice\n')
if(first_choice!='-'):
    print('Service 1:', first_choice +',', '$'+str(autoshop[first_choice]))
    total+=autoshop[first_choice]
else:
    print('Service 1:', autoshop[first_choice])
if(second_choice!='-'):
    print('Service 2:', second_choice+',', '$'+str(autoshop[second_choice]))
    total+=autoshop[second_choice]
else:
    print('Service 2:', autoshop[second_choice])
print('\nTotal: $%d' % total)