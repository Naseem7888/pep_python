# Program 1 Try Exception
# a = 10
# b = 0
# try:
#     d = a/b
#     print(d)
#     print("This will not execute")
#     print("This will execute only if no exception occurs")

# except ZeroDivisionError:
#     print("Inside except block")

# print("This will execute and Rest of the code will execute")




# Program 2 Try Exception program
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# try:
#     d = a / b
#     print(f"The result is: {d}")
#     print("This will not execute if an exception occurs")

# except ZeroDivisionError:
#     print("You cannot divide by zero. Please enter a valid denominator.")



# Program 3 Try Except Else
# a = 10
# b = 5
# try:
#     d = a / b
#     print(d)
#     print("Inside try")

# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# else:
#     print("Inside else")

# print("Rest of the code")


# Program 4 Try Except Finally
# a = 10
# b = 0
# try:
#     d = a / b
#     print(d)
#     print("Inside try")

# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# else:
#     print("Inside else")

# finally:
#     print("Inside finally")

# print("Rest of the code")



# Program 5 Except Multiple Exceptions
# a = 10
# b = 0
# try:
#     d = a / b
#     print(d)

# except (NameError, ZeroDivisionError) as obj:
#     print(obj)

# print("Rest of the Code")


# Program 6 Extra Exception Handling
# class TooYoungException(Exception):
#     def __init__(self, arg):
#         self.msg = arg

# class TooOldException(Exception):
#     def __init__(self, arg):
#         self.msg = arg

# try:
#     age = int(input("Enter your age: "))

#     if age < 18:
#         raise TooYoungException("Plz wait some more time, you will get the best match soon!!")
#     elif age > 60: # Changed from 18 to 60 for "too old"
#         raise TooOldException("Your age already crossed marriage age... no chance of getting.")
#     else:
#         print("You will get match details soon by email!!!")

# except ValueError:
#     print("Invalid input. Please enter a valid number for your age.")
# except TooYoungException as e:
#     print(f"Error: {e.msg}")
# except TooOldException as e:
#     print(f"Error: {e.msg}")
# except Exception as e: # General catch-all for any other unexpected errors
#     print(f"An unexpected error occurred: {e}")

# print("Program finished.")


# Program 7 File Handling
# f = open ('student.txt', mode='w')
# f.write('hello \n')
# f.write('PythonTraning\n')
# f.write('how are you')
# f.close()
# print('writting succes')


# program 8
# f= open ("student.txt", mode='r')
# f.close()

# program 9 file handling reading line by line
# name = input ('enter your name')
# age = input ('enter your age')
# f= open ("student.txt", mode='w')
# f.write (f"Name: {name}\n")
# f.write (f"Age: {age}\n")
# f.close()
# f = open("student.txt", mode='r')
# content = f.read()
# f.close()
# print(content)
