##Kyler Telge 1825829
print('Enter wall height (feet):')
height = int(input())
print('Enter wall width (feet):')
width = int(input())
area = height*width
cans = 1
colordict = {"red": 35, "blue": 25, "green": 23}
paint = 350
needed = area/paint
while(needed > cans):
    cans+=1
print('Wall area:', area, 'square feet')
print('Paint needed:', '{:.2f}'.format(needed), 'gallons')
print('Cans needed:', cans,'can(s)\n')
print('Choose a color to paint the wall:')
color=input()
print('Cost of purchasing', color, 'paint:', '$'+str(colordict[color]*cans))
