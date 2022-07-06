str_txt='WELCOME TO PYTHON CORE!'

#Cau 2
print(str_txt[:3])
print(str_txt[-4:])
print(str_txt[1:5])
print(str_txt[:5])
print(str_txt[1:-1])


#Cau 3
for index, i in enumerate(str_txt):
    print(i)

#Cau 4 
print(len(str_txt))

#Cau 5
get_check=input('Enter string: ')
if get_check in str_txt:
    print(str_txt.index(get_check))
else:
    print('No substring')

#Cau 6
print(str_txt.upper())
print(str_txt.lower())
print(str_txt.title())

#Cau 7
print(str_txt.replace(' ',''))

#Cau 8
print(str_txt.replace('h','m'))

#Cau 9
pt=str_txt.split(' ')
print(pt[1])