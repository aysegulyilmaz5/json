import json

data = '{"firstName" : "Aysegul","lastName":"Yilmaz"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])

customer = {
  "firstName" : "Aysegul",
  "email" : "aysegulyilmaz@gmail.com"
}

customerJson = json.dumps(customer)

print(customer)
