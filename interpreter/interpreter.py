
x, y, z = input("Expression: ").split(" ")

if y == "+":
    sol = float(x) + float(z)
    print("{:.1f}".format(sol))
elif y == "-":
    sol = float(x) - float(z)
    print("{:.1f}".format(sol))
elif y == "*":
    sol = float(x) * float(z)
    print("{:.1f}".format(sol))
elif y == "/":
    sol = float(x) / float(z)
    print("{:.1f}".format(sol))

