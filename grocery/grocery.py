gList = {}

while True:
    try:
        item = input()
    except EOFError:
        print()
        break
    if item.upper() in gList:
        gList[item.upper()] += 1
    else:
        gList[item.upper()] = 1

for item in sorted(gList.keys()):
    print(gList[item], item)

