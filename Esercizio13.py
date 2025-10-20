import json


d={ "nome": "Luca", "eta'": 25}

json_string = json.dumps(d) #serializing 

print(json_string)


json_string2 = '{ "nome": "Luca", "età": 25}'

data = json.loads(json_string2)


#Function= dictionaries to JSON str + save on the file 
with open("corso.json", "w") as file:
    json.dump(d, file)


with open("corso.json", "r") as file:
    datas = json.load(file)