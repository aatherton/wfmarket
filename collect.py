### import dependancies ###

import statistics
import requests

### declare globals ###

HEADERS = {"accept": "application/json", "Platform": "pc"}
BASE = "https://api.warframe.market/v1/items"

### define functions ###

### main logic ###

# query to get list of items
items = requests.get(BASE, headers=HEADERS).json()["payload"]["items"]
# declare result as empty dict
result = {}
for each in items:
  # query to get orders for that item
  query = requests.get(f"{BASE}/{each['url_name']}/orders", headers=HEADERS).json()["payload"]["orders"]
  # select platinum where order_type = "buy"
  pipe = []
  for other in query:
    if other['order_type'] == "buy":
      pipe.append(other['platinum'])
  # get mode
  try:
    pipe = statistics.mode(pipe)
  except:
    pipe = 0
  # add {each.url_name: mode} to result
  result[each.url_name] = pipe
return result
