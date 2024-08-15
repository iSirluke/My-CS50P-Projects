answer = input("What is the Answer to the GReat Question of Life, the Universe, and Everything?: ").lower().strip()

if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
else:
    print("No")
