# def greet():
#     print("Hello")
# greet()

# greet = lambda : "Hello"
# print(greet())



# def add(a , b):
#     print( a + b)
# add(10 , 20)

# add = lambda a , b : a + b
# print(add(10,20))


# def oddOrEven(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"    
# print(oddOrEven(8))


oddOrEven = lambda n : "Even" if n % 2 == 0 else "Odd"
print(oddOrEven(8))