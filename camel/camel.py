camel = input("camelCase text: ")

snake = ""

for i in range(len(camel)):
    if camel[i].isupper():
        snake = snake + '_' + camel[i].lower()
    else:
        snake += camel[i]


print("snake_case text: ", snake)