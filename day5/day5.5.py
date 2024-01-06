#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

num_random_letters = nr_letters
random_letters = random.sample(letters, num_random_letters)

num_random_numbers = nr_numbers
random_numbers = random.sample(numbers, num_random_numbers)

num_random_symbols = nr_symbols
random_symbols = random.sample(symbols, num_random_symbols)


total_password = random_letters + random_numbers + random_symbols
num_total_password = len(total_password)
generate_password = random.sample(total_password, num_total_password)

password = ""
for char in generate_password:
    password += char
print (f"Your Password is: {password}")