import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= round(random.randint(1, 6)) 
nr_symbols = round(random.randint(1,7))
nr_numbers = round(random.randint(1,8))

password_list = []

for letter in range(1, nr_letters+1):
  rand_letter = random.choice(letters)
  password_list.append(rand_letter)

for letter in range(1, nr_symbols+1):
  rand_symbol = random.choice(symbols)
  password_list.append(rand_symbol)

for num in range(1, nr_numbers+1):
  rand_number = random.choice(numbers)
  password_list.append(rand_number)


random.shuffle(password_list)

password =""

for char in password_list:
  password += char 
print(f"your password is {password}")


