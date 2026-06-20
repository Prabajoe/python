def greet_users(**kwargs):
    # kwargs is a dictionary: {'name': 'Alice', 'role': 'Admin'}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
greet_users(name="Alice", role="Admin")
greet_users(user_id=101, status="Active", location="New York")
greet_users(name= "satheesh", course="DA" , status=True , id = 101)


def create_user(**kwargs):
    print("User created with data:", kwargs)
create_user(name="John", email="john@gmail.com", age=25)