# The *args parameter allows a function to take any number of positional arguments


def greet(*name):
    print(name)
greet("Satheesh", "Maarison" , "Ram" , "John" , "Seetha")



def add(a,*b):
    print(a + sum(b))
add(10, 20 , 50, 40 , 39 , 39)



def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))