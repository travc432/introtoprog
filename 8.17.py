#Travis and Ron

team = {}
i = 1
while i <= 5:
    jersey = int(input('Enter player %i\'s jersey number:\n' % i))
    rating = int(input('Enter player %i\'s rating:\n' % i))
    team[jersey] = rating
    i += 1

print('ROSTER')
for jersey in sorted(team):
    print('Jersey number: %i, Rating: %i' % (jersey, team[jersey]))


def add_player():
    new_jersey = int(input('Enter a new player\'s jersey number:\n'))
    new_rating = int(input('Enter a new player\'s rating:'))
    team[new_jersey] = new_rating
    menu()

def remove_player():
    removed_jersey = int(input('Enter a jersey number:'))
    del team[removed_jersey]
    menu()


def update_rating():
    rating_jersey = int(input('Enter a jersey number:'))
    rating_update = int(input('Enter a new rating for player:'))
    team[rating_jersey] = rating_update
    menu()


def output_above():
    min_rating = int(input('Enter a rating:'))
    print('ABOVE %i' % min_rating)
    for jersey in team:
        if team[jersey] > min_rating:
            print('Jersey number: %i, Rating: %i' % (jersey, team[jersey]))
    menu()


def output_roster():
    print('ROSTER')
    for jersey in sorted(team):
        print('Jersey number: %i, Rating: %i' % (jersey, team[jersey]))


def quit():
    exit()


def menu():

    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')

    command = input('Choose an option:')

    if command == 'a':
        add_player()
    if command == 'd':
        remove_player()
    if command == 'u':
        update_rating()
    if command == 'r':
        output_above()
    if command == 'o':
        output_roster()
    if command == 'q':
        exit()
    else:
        menu()


menu()