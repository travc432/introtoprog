#Travis Crotteau and Ron Williams
dict = {'A': 2, 'a': 2, 'B': 2, 'b': 2, 'C': 2, 'c': 2, 'D': 3, 'd': 3, 'E': 3, 'e': 3, 'F': 3, 'f': 3, 'G': 4, 'g': 4, 'H': 4, 'h': 4, 'I': 4, 'i': 4, 'J': 5, 'j': 5, 'K': 5, 'k': 5, 'L': 5, 'l': 5, 'M': 6, 'm': 6, 'N': 6, 'n': 6, 'O': 6, 'o': 6, 'P': 7, 'p': 7, 'Q': 7, 'q': 7, 'R': 7, 'r': 7, 'S': 7, 's': 7, 'T': 8, 't': 8, 'U': 8, 'u': 8, 'V': 8, 'v': 8, 'W': 9, 'w': 9, 'X': 9, 'x': 9, 'Y': 9, 'y': 9, 'Z': 9, 'z': 9}


def translation(letters):
    number = ''
    for char in letters:
      if char.isalpha():
        number += str(dict[char.upper()])
      if char.isdigit():
        number += str(char)
    return number

def main():
    user_input = str(input("Please enter a 10 digit telephone number in the format XXX-XXX-XXXX and use some letters!: "))
    print("You entered: {}" .format(user_input))
    print("You get: {}" .format(translation(user_input)))

main()21