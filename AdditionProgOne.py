#Travis Crotteau and Ron Williams

full_name = input("What is your full name?\n")
name_list = full_name.split(" ")
first_init = name_list[0][0]
second_init = name_list[1][0]
third_init = name_list[2][0]

print('%s. %s. %s. ' % (first_init, second_init, third_init))

