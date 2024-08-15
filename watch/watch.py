import re
import sys

def main():
    print(s)

def parse(s):
    url = input("HTML: ").strip()
    if matches := re.search(r"^(<iframe)?.+(src=.https?)://(?:www\.)?youtube\.com/(embed)?/([a-zA-Z0-9]).+\w*(</iframe>)?$", url, re.IGNORECASE):
            s = ("https://youtu.be/:", matches.group(5))
            return s

if __name__ == "__main__":
    main()