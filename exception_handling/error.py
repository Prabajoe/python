# try
# except
# else
# finally


# try:
#     num=int(input("enter number"))

#     x=10/num
#     print(x)

# except ValueError as e:
#     print(e)

# except Exception as e:
#     print(e)

# else:
#     print("program executed")

# finally:
#     print("exception handled")



# sum=10+10
# print(sum)

class AgeError(Exception):
   
   pass

try:
     
    age=int(input("ente your age "))
      
    if age<18:
        raise AgeError("not eligble age to vote")
    
    print("valid")
       
except AgeError as e:
 print(e)    

 

