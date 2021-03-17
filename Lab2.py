import json
import time
import requests


def currencyOutput():
    x = requests.get('https://blockchain.info/ru/ticker').text
    return x
print("Enter currency: ")
x = input()

while True:
    d1 = json.loads(currencyOutput())
    d2 = d1[x]
    print(d2["buy"])
    time.sleep(5)