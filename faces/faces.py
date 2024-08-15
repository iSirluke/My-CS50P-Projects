def main():
    message = input("Type your message: ")
    result = convert(message)
    print(result)

def convert(message):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return message

main()