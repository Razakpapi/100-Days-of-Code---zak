import random
names_string = input("Type everybody\'s names, separated by a comma. \n")

names = names_string.split(", ")

# num_items = len(names)

# random_name = random.randint(0, num_items - 1)
# who_will_pay = names[random_name]

who_will_pay = random.choice(names)

print(who_will_pay + " will pay the bill")

