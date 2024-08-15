
def main():
    word = str(input("Input: "))
    wordWithOutVowels = shorten(word)
    print("Output: ", wordWithOutVowels)

def shorten(word):
    wordWithOutVowels = ""
    for letter in word:
        wordWithOutVowels = (word.translate({ord(i): None for i in 'aAeEiIoOuU'}))
    return wordWithOutVowels

if __name__ == "__main__":
    main()
