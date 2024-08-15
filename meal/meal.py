def main():
    time = input("What time is it?: ")
    f_time = convert(time)

    if f_time >= 7 and f_time <= 8:
        print("Breakfast Time")
    elif f_time >= 12 and f_time <= 13:
        print("Lunch Time")
    elif f_time >= 18 and f_time <= 19:
        print("Dinner Time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes) / 60)
    return hours




if __name__ == "__main__":
    main()