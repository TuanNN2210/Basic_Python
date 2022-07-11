
str_txt = input('Enter the string: ')
count = 0

for i in str_txt:
    if i == 't' or i == 'T':
        count += 1 

print(f'The number of times that the letter T (uppercase or lowercase) appears: {count}')