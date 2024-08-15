def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        index = fraction.find("/")
        try:
            a = int(fraction[:index])
            b = int(fraction[index+1:])
            fraction = a / b
            if a > b:
                fraction = input("Fraction: ")
                continue
            else:
                percentage = int(fraction * 100)
                return percentage

        except(ValueError, ZeroDivisionError):
            continue

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(round(percentage)) + "%"

if __name__ == "__main__":
    main()


