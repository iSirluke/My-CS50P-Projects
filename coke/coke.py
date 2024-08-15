total = 50
print("Amount Due:", total)

amnt_due = 50
coins = 0

while True:
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        amnt_due -= coin
        coins += coin

    if coins >= 50:
        print("Change Owed:", (coins - 50))
        break

    else:
        print("Amount Due:", (amnt_due))








