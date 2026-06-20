mydictionary = { "name" : "Satheesh" , "Gender" : "Male" , "IsActive" : True , "ID" : 101}
# print(mydictionary)

# You can access the items of a dictionary by referring to its key name
# print(mydictionary["IsActive"])

# x = mydictionary.get("Gender")
# print(x)



# Changing Element
# mydictionary["IsActive"] = False
# mydictionary["IsActive"] = True


# Getting Keys
# print(mydictionary.keys())
# print(mydictionary.values())
# print(mydictionary.items())


# Iteration
# for i in mydictionary:
#     print(i)

# for i in mydictionary.values():
#     print(i)



# Update()
# mydictionary.update({"ID" : 102})
# print(mydictionary)


# mydictionary["Town"] = "Pondicherry"
# mydictionary.update({"Age": 25})
# print(mydictionary)


# Removing Values
# print(mydictionary)
# mydictionary.pop("ID")
# print(mydictionary)


# print(mydictionary)
# mydictionary.popitem()
# print(mydictionary)


# del mydictionary["Gender"]
# print(mydictionary)
# del mydictionary
# print(mydictionary)



# print(mydictionary)
# mydictionary.clear()
# print(mydictionary)