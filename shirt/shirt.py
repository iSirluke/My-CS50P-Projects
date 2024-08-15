import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    exts = [".jpg", ".jpeg", ".png"]
    ext1 = os.path.splitext(sys.argv[1])
    ext2 = os.path.splitext(sys.argv[2])
    if ext1[1] == ext2[1] and ext1[1] in exts:
        try:
            jpgfile = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Input does not exist")

        shirt = Image.open("shirt.png")
        size = shirt.size
        muppet = ImageOps.fit(jpgfile, size)
        muppet.paste(shirt, shirt)
        muppet.save(sys.argv[2])
    elif ext1[1] != ext2[1]:
        sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguements")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguements")