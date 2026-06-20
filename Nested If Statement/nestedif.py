username = input(" Please Enter Your User Name: ")
password = input("Please Enter Your Password: ")

correct_username = "python"
correct_password = "India@2026"


if username == correct_username:
    if password == correct_password:
        print("Login Successfull")
    else:
        print("Invalid Password")
else:
    print("Invalid User Name")