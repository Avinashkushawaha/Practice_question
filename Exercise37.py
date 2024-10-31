#wap to check string lower character or not
string = input('Enter character here: ')
lower = True

for char in string:
    if not char.islower():
        lower = False
        break
if lower:   
    print(' it is  lowercase character')   
else:
    print('it is not lowercase characters')



