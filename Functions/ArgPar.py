# # Parameter: The variable listed inside the parentheses when you define a function. It acts as a placeholder.
# # Argument: The actual value or data you pass to the function when you call it.

# def greet(name , course="Enquiry"):
#     print(f"Hello {name} Welcome to {course} class")

# greet("Satheesh", "Data Analytics")
# greet("Maarison" , "Python FS")
# greet("John" , "MERN")

# # Positional Arguments: These are matched to parameters based on their order. The first argument goes to the first parameter, and so on.
# greet("python", "ram")



# # Keyword Arguments: You pass values by explicitly naming the parameter (e.g., greet(name="Alice")). This allows you to ignore the order of parameters.
# greet(course="Python",name= "Ram")


# # Default Parameters: You can assign a default value to a parameter in the definition. If an argument isn't provided during the call, the default is used.

# greet("John")

# def add(a, b=0):
#     print(a + b)
# add(10)




# In Python, the primary difference is that print() displays information to the user, while return sends data back to the program to be used later


def greetings(name):
    print(f"Hello {name}")
    print("Hello")


greetings("Satheesh")









