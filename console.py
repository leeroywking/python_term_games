import os
import time
import requests
import json
import math

while True:
    size = os.get_terminal_size()
    first = "".join(["-" for i in range(size.columns)])
    quote = json.loads(requests.get("https://bad-guy-quotes.herokuapp.com/").content)[0]
    quote_lines = math.ceil(len(quote) / size.columns)
    print(first)
    print(quote)
    for i in range(size.lines - 3 - quote_lines):
        print("")
    print(first)
    time.sleep(5)
