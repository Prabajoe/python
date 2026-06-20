from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["Employee"]
collection=db["emp"]

print("connect successfully")

while True:
    print("1.insert")
    print("2.view")
    print("3.update")
    print("4.delete")
    print("5.exit")

    choice=int(input("Enter your choice"))


    if choice==1:

        name=input("enter the name")
        age=input("enter the age")

        collection.insert_one({
            "name":name,
            "age":age
        })

        print("inserted Successfully")

    elif choice==2:

        for data in collection.find():
            print(data)

    elif choice==3:

        name=input("enter the name")
        newage=int(input("enter the age"))

        collection.update_one(
            {"name":name},
            {"$set":{"age":newage}}
            )

    elif choice==4:

        name=input('enter the name')

        collection.delete_one({"name":name})

    elif choice==5:
        break
    else:
        print("Invalid choice")


          

          