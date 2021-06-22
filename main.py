import json
from processor import process

with open("./config.json") as json_data_file:
    data = json.load(json_data_file)
print('based on V1 Bitt PyShell')
print(data["start_message"])
while True:
    x = input(data["shell_name"])
    process(x)
