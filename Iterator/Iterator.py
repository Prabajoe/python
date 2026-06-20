name="Satheesh ravi"

item=iter(name)


while True:

    try:
        print(next(item))
    except StopIteration:
        break

