#Travis Crotteau and Ron Williams

def get_names():
    names = input('Enter input string:\n')
    if names != 'q':
        while ',' not in names:
            print('Error: No comma in string.\n')
            get_names()
        names = names.replace(" ","")
        names_list = names.split(",")
        print('First word: {}'.format(names_list[0]))
        print('Second word: {}\n'.format(names_list[1]))
        get_names()
    else:
        exit()
get_names()