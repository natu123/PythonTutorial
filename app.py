# print("Kenji")
# print('o----')
# print(' ||||')
# print('*' * 10)

# price = 10    #integer : int
# rating = 4.9    #float
# name = "Kenji"  #String : str
# is_published = True    #boolean value

# name = input('What is your name? ')
# print('Hi ' + name)

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2023 - int(birth_year)     #subtraction
# print(type(age))
# print(age)
# # int()
# # float()
# # bool()

# weight_lbs = input('Wight(lbs): ')   #pounds, lbs
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# course = '''
# Hi, John,
#
# Here is our first email to you.
#
# Thank you,
# The support team
# '''
# print(course)

# # index
# course = 'Python for Beginners'
# slice = course[1:-1]
# print(slice)

# #Formatted Strings      f-strings
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f"{first} [{last}] is a coder"
# print(msg)

# # String Methods
# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course)
# print(course.find('r'))
# print(course.replace('Beginners', 'Absolute Beginners'))
# print(course)
# print('Python' in course)

# # Arithmetric Operations
# # integers are whole numbers and floating point numbers(floats) what are numbers with a decimal point.
# print(10 + 3)        #additoin
# print(10 - 3)        #subtraction
# print(10 * 3)       #multiplication
# print(10 / 3)
# print(10 // 3)      #divisions
# print(10 % 3)       #modulus == reminder of division
# print(10 ** 3)      #exponent
# #Augmented Assignment Operator
# x = 10
# x = x + 3
# x += 3      #incremented
# print(x)

#Operator Precedence
#parenthesis
#exponentiation
#multiplicatoni or division
#additoin or subtraction

# #Math Functions
# x = 2.5
# print(round(x))
# print(abs(-1))
# #Math modules
# import math
# print(math.ceil(2.1))
# print(math.floor(2.1))



# #If Statement
# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
#
# print("Enjoy your day")

# Price of a house is $1M.
# If buyer has good credit,
#     they need to put down 10%.
# Otherwise
#     they need to pud down 20%.
# Print the down payment.

# price = 1000000
# has_good_credit = False
#
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")



# #Logical Operators
# has_high_income = True
# has_good_credit = False
# has_criminal_record = False
#
# if has_high_income or has_good_credit:     #and / or
#     print("Eligible for loan")
#
# if has_high_income and not has_criminal_record:
#     print("Eligible for loan")
#
# # AND: both
# # OR: at least one
# # NOT



#Comparison Operators
# temperature = 30
#
# if temperature >= 30:       #=: assignment operator
#     print("It's a hot day")
# else:
#     print("It's not a hot day")
#
# name = input("Input your name: ")
#
# if len(name) < 3:
#     print("Name must be at least 3 characters.")
# elif len(name) > 50:
#     print("Name must be a maximum of 50 characters.")
# else:
#     print("Name looks good!")



# #Project: Weight Converter
# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f'You are {converted} kilos.')
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds.")



# #While Loops
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# print("Done")



# #Guessing Game
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess number: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('Sorry, you failed!')



# #Car Game
# command = ""
# started = False
#
# while True:        #DRY = Don't repeat yourself.
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that.")



# For Loops
# for item in 'Python':
# for item in ["Mosh", "John", "Sarah"]:
# for item in range(5, 10, 2):
#     print(item)



# prices = [10, 20, 30]
# total = 0
#
# for price in prices:
#     total += price
# print(f"Total: {total}")



# # Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(F'({x}, {y})')



# numbers = [5, 2, 5, 2, 2]
#
# # for num in numbers:
# #         print("*" * num)
#
# for x_count in numbers:
#     output=''
#     for count in range(x_count):
#         output += 'x'
#     print(output)



# # Lists
# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names[1:-1:2])
# print(names)



# nums = [3, 6, 2, 8, 4, 10, 3]
# max = nums[0]
#
# for num in nums:
#     if num > max:
#         max = num
# print(max)



# # 2D Lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# # matrix[0][1] = 20
# # print(matrix[0][1])
#
# for row in matrix:
#     print(row)
#     # for item in row:
#     #     print(item)



# # List Methods(List Functions)
# nums = [5, 2, 1, 2, 4]
# nums.append(20)
# nums.insert(1, 10)
# nums.remove(2)
# # nums.clear()
# print(nums)
# nums.pop()
# print(nums)
# print(nums.index(2))
# print(50 in nums)
# nums.insert(1, 2)
# nums.insert(1, 2)
# print(nums)
# print(nums.count(2))
# nums.reverse()
# print(nums)
# print(nums.sort())
# print(nums)
#
# print('*' * 10)
# nums2 = nums.copy()
# nums.append(10)
# print(nums)
# print(nums2)



# nums = [2, 2, 4, 6, 3, 4, 6, 2, 1]
# uniques = []
#
# for num in nums:
#     if num not in uniques:
#         uniques.append(num)
# print(uniques)



# # Tuples
# # Tuples are immutable.
# nums = (1, 2, 3)
# # nums[0] = 10
# print(nums[0])



# # Unpacking
# coordinates = (1, 2, 3)
#
# # print(coordinates[0] * coordinates[1] * coordinates[2])
# #
# # x = coordinates[0]
# # y = coordinates[1]
# # z = coordinates[2]
# # print(x * y * z)
#
# x, y, z = coordinates
# print(y)



# # Dictionaries
# # Name: John Smith
# # Email: john@gmail.com
# # Phone: 1234
# customer = {        #key value pair can't be duplicated.
#     "name": "John Smith",
#     "age": 30,
#     "is_verifies": True
# }
# print(customer["name"])
# print(customer.get("birthdate"))
# print(customer.get("birthdate", "Jan 1 1980"))
# print(customer.get("name", "Jan 1 1980"))
#
# customer["name"] = "Cary Brilliant"
# print(customer["name"])
#
# customer["birthdate"] = "1990-08-01"
# print(customer["birthdate"])



# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
#
# output = ""
# for character in phone:
#     output += digits_mapping.get(character, "!") + " "
# print(output)



# # Emoji Converter :)
# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)": "😋",
#     ":(": "😢"
# }
#
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)



# # Functions
# def greet_user():
#     print('Hi there!')
#     print('Welcome aboard')
#
#
# print("Start")
# greet_user()
# print("Finish")



# # Parameters
# def greet_user(first_name, last_name):       #parameters and arguments
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# print("Start")
# greet_user('John', 'Smith')
# greet_user('Mary', 'Japsen')
# print("Finish")



#Keyword Arguments

