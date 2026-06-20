# The match case statement, introduced in Python 3.10, is a form of structural pattern matching used to compare an expression's value to a series of patterns and execute the code block of the first pattern that matches.

# Syntax: 

# match express:
#     pattern 1
#        block of code
#     pattern 2
#         block of code 
#     case _:
#         block of code


# name = input(" Please Enter Your Stack: ")

# match name:
#     case "Java":
#         print(" Its Java")
#     case "MERN":
#         print("Its MERN")
#     case "Python":
#         print("Its Python")
#     case _:
#         print("No Match Found")
# print((4+5)*5**(4-2));



my_letter = input(" Please Type a Letter to check if it is Vowel or Not : ")

match my_letter:
    case "a" | "e" | "i" | "o" | "u" :
        print("The Letter is a Vowel")
    case _:
        print(" The Letter is not a vowel")




