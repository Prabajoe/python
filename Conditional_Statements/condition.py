# Python conditional statements are used to make decisions in code by executing specific blocks of code based on whether a condition is True or False


# if statement: The simplest form, which runs a code block only if its condition is True

# else statement: Provides an alternative block of code to run if the if condition is False

# elif statement: Allows you to check multiple conditions sequentially. The first condition that evaluates to True has its code block execute25d, and the rest are skipped.

# Syntax



# num = int(input("Please Enter a Number to Check ODD or EVEN:   "))

# if num % 2 == 0 :
#     print(" Its A Even Number")
# else:
#     print("Its a odd Number")



# mark = int(input("Please Enter Your Mark: "))

# if mark >= 40 and mark  <= 50:
#     print("You are A+ Grade")
# elif mark >= 20 and mark < 40:
#     print("You are A Grade")
# else:
#     print("You are Failed")




num1 = int(input("Enter a First Number: "))
num2 = int(input("Enter a Second Number: "))

if num1 > num2:
    print(" Both are Equal")
else:
    print("Not Equal")

