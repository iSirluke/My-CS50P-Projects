import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^((25[0-5]|2[0-4][\w]|1[\w][\w]|[1-9]?[\w])\.){3}(25[0-5]|2[0-4][\w]|1[\w][\w]|[1-9]?[\w])$", ip):
        nums = ip.split(".")
        for num in nums:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()