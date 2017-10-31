#Travis Crotteau
data_title = input('Enter a title for the data:\n')
print('You entered: {}\n' .format(data_title))

col_one = input('Enter the column 1 header:\n')
print('You entered: {}\n' .format(col_one))

col_two = input('Enter the column 2 header:\n')
print('You entered: {}\n' .format(col_two))

data_strings = []

data_integers = []

while True:
    user_input = input('Enter a data point (-1 to stop input):\n')
    split_data = user_input.split(',')
    if user_input == '-1':
        print()
        break
    elif ',' not in user_input:
        print('Error: No comma in string.\n')
    elif user_input.count(',') >= 2:
        print('Error: Too many commas in input.\n')
    elif split_data[1].replace(' ','').isdigit() == False:
        print('Error: Comma not followed by an integer.\n')
    else:
        print('Data string: {}' .format(split_data[0]))
        print('Data integer: {}\n' .format(split_data[1].replace(' ', '')))
        data_strings.append(split_data[0])
        data_integers.append(split_data[1])
print('%33s' % data_title)
print('%-20s|%23s' % (col_one, col_two))
for i in range(44):
    print('-', end='')
print()
for i in range(len(data_strings)):
    print('%-20s|%23s' % (data_strings[i], data_integers[i]))

print('')
for i in range(len(data_strings)):
    print('%20s' % data_strings[i], end=' ')
    print('*' * int(data_integers[i]))



