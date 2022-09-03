from collections import Counter
first_Dictionary = {}
second_Dictionary = {}
max_length = 3

while len(first_Dictionary) < max_length:
    letter = input("Enter letter: ")
    value = int(input("Enter value: "))
    first_Dictionary[letter] = value


print("Beginning second Dictionary: ")

while len(second_Dictionary) < max_length:
    letter = input("Enter letter: ")
    value = int(input("enter value: "))
    second_Dictionary[letter] = value

last_Dictionary = Counter(first_Dictionary) + Counter(second_Dictionary)

print(repr(last_Dictionary).strip('Counter()'))