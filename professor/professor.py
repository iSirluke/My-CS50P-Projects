import random

def main():
    level = get_level()
    score = game(level)
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

def play(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            result = int(input(f"{x} + {y} = "))
            if result == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

def game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        answer = play(x,y)
        if answer == True:
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()
