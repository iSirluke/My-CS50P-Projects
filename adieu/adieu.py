import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")

    except EOFError:
        print()
        break
    names.append(name)

text = p.join(names)

print("Adieu, adieu, to " + text)


