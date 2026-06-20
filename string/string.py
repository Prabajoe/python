# # A string in Python is an immutable sequence of Unicode characters used to store and manipulate text data.


# name = "Python"
# a = 'Python'

# anothername = """ A string in Python is an immutable sequence of Unicode 
# characters used to store and manipulate text data. """


# # Indexing in Python is the process of accessing individual elements within a sequence data type (such as a string, list, or tuple) using their numerical position, or index.

# greetings = "WELCOME"
# print(greetings[3], "Index")


# # The len() function in Python is a built-in utility that returns the number of items in an object.
# print(len(greetings),"Lenghth")

# # Looping a String
# for i in greetings:
#     print(i)


# String and Its Methods:

# # Formatting String - In Python, string formatting is the process of dynamically inserting variables or expressions into a string to create a structured and readable output
# name = "Satheesh"
# print("Welcome" , name)
# print("Welcome " + name)
# print(f"Welcome {name}")


# # In Python, the if-else shorthand (officially known as a conditional expression or ternary operator) allows you to write conditional logic in a single line

# num = 18
# if num >= 18:
#     print(" Eligible to Vote")
# else:
#     print("Not Eligibel to Vote")


# print("Eligile to Vote") if num >= 18 else print(" not eligible to Vote")



# # lower - The lower() method converts all uppercase alphabetic characters in a string to lowercase

# a = "HELLO WORLD"
# print(a.lower())

# # upper() method in Python is a built-in string method that converts all lowercase letters in a string to uppercase
# b = "hello world"
# print(b.upper())

# print(b.title())

# txt = "banana"
# x = txt.center(20)
# print(x)
# print(len(x))


# name = "Hello Python"
# newname = name[6:12:2]
# print(newname)


# for i in name:
#     print(i)


# reversedstring = name[::-1]
# print(reversedstring)