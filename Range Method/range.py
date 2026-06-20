# The Python range() function generates an immutable sequence of integers and is commonly used to control loops.

# range(start, stop, step)


# One argument (stop): Creates a sequence from 0 to the specified number minus one, incrementing by 1.
# for i in range(11):
#     print(i)


# Two arguments (start, stop): Creates a sequence from start up to, but not including, stop, incrementing by 1.
# for i in range(1,11):
#     print(i)


# Three arguments (start, stop, step): Creates a sequence from start up to, but not including, stop, using the specified step size.
# for i in range(2,11,2):
#     print(i)


# for i in range(1,11,2):
#     print(i)


# Counting backward: Use a negative step value to count down. The start value must be greater than the stop value
# for i in range(10,0, -2):
#     print(i)



# for i in range(3):
#     print("Python")


# # A for loop in Python is used for iterating over a sequence

# for i in "Data Analytics":
#     print(i)



# name = "Data Analytics"
# for i in name:
#     print(i)


# for i in range(1,51):
#     if i % 5 == 0:
#         print(i)

for i in range(1,201):
    if i % 4 == 0 and i % 8 == 0:
        print(i)