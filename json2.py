import json 

with open("user.json") as users:
  data = json.load(users)
  print(data)
