def string_strip(str):
 if len(str) < 2:
    return 'String is too short!'
 return str[0:2] + str[-2:]


user_word = input('Please enter a string: ')
returnString = string_strip(user_word)
print(returnString)