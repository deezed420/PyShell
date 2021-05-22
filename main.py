import json
from processor import process

with open("./config.json") as json_data_file:
    data = json.load(json_data_file)
    start_message = data["start_message"]
    consolename = data["shell_name"]

print('based on V1 Bitt PyShell')
print(start_message)
while True:
    x = input(consolename)
    process(x)
