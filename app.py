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



#Project: Weight Converter
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f'You are {converted} kilos.')
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds.")