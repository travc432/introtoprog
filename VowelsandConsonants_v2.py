# Travis Crotteau and Ron Williams

def num_vowels(user_string):
    num_vowels = 0
    for i in user_string.lower():
        if (i == 'a' or
            i == 'e' or
            i == 'i' or
            i == 'o' or
            i == 'u' or
                i == 'y'):
            num_vowels += 1
    print('The number of vowels in %s is %i' % (user_string, num_vowels))

def num_consonants(user_string):
    num_consonants = 0
    for i in user_string.lower():
        if (i == 'b' or
            i == 'c' or
            i == 'd' or
            i == 'f' or
            i == 'g' or
            i == 'h' or
            i == 'j' or
            i == 'k' or
            i == 'l' or
            i == 'm' or
            i == 'n' or
            i == 'p' or
            i == 'q' or
            i == 'r' or
            i == 's' or
            i == 't' or
            i == 'v' or
            i == 'w' or
            i == 'x' or
            i == 'z'):
            num_consonants += 1
    print('The number of consonants in %s is %i' % (user_string, num_consonants))


user_string = input('Gimme a string! ')
num_vowels(user_string)
num_consonants(user_string)