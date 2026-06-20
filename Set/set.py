# myset  = {"Apple", "Banana", "Grapes", "Apple", 0 , True, 1, False}


# # Set Methods

# # 1. 1. Adding elements to Sets: add() function is used to insert new elements into a set. It automatically ignores duplicates.

# # myset.add("Python")
# # print(myset)



# # # 2. Union of Sets: union() function combines two sets and returns a new set with all unique elements.
# # setone = {"a", "b", "c"}
# # settwo = {"d", "e", "a"}

# # setthree = setone.union(settwo)
# # setthree = setone | settwo


# # print(setthree)


# # # 3. Intersection of Sets: intersection() function returns a new set containing elements that are common to both sets

# # a = {1, 2, 3}
# # b = {2, 3, 4}
# # # i = a.intersection(b)
# # i = a & b
# # print(i)

# # # # 4. Difference of Sets: difference() function returns a set containing elements that are in the first set but not in the second.

# # # k = a.difference(b)
# # k = a - b
# # print(k)



# # # 5. Clearing a Set: clear() function removes all elements from a set, leaving it empty
# s = {1, 2, 3,4,46467, 5757,5467}
# # s.clear()
# # print(s)



# # s.pop()
# # print(s)


# fruits = {"apple", "banana", "cherry"}

# fruits.remove("banana")

# print(fruits)


a = frozenset({"apple", "banana", "grapes"})
b = {1,2,3,4,5}
print(type(a))
print(type(b))