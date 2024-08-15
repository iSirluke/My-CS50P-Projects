import sys
import csv

output = []
try:
  with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
      splitName = row["name"].split(",")
      output.append({'first': splitName[1].lstrip(), "last": splitName[0], "house": row["house"]})
except FileNotFoundError:
  sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
  writer.writerow({"first": "first", "last": "last", "house": "house"})
  for row in output:
    writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

  if len(sys.argv) < 3:
    sys.exit("Too few command-line arguements")
if len(sys.argv) > 3:
  sys.exit("Too many command-line arguements")
if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
  sys.exit("Not a CSV file")

