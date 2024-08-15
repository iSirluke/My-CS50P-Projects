import requests
import sys

if len(sys.argv) == 2:
    try:
        val = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total = bitcoin * val
    print(f"${total:,.4f}")
except requests.ResponseException:
    print("RequestException")
    sys.exit(1)
