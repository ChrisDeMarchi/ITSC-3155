first_num = input('Please enter the lower number: ')
second_num = input('Please enter the higher number: ')
first_num = int(first_num)
second_num = int(second_num) + 1
stuff = range(first_num, second_num)
for n in stuff:
    if n % 7 == 0 and n % 5 != 0:
        print(n, end=", ")
