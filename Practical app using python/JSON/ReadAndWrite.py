stringOfJsonDate = '{"Name": "Majid", "age": "one year", "Ischild": true}'
import json

# read

ReadJsonValue = json.loads(stringOfJsonDate)
print(ReadJsonValue)
print(type(ReadJsonValue))

# Write
MysonInfo = {"Name": "Majid", "age": "one year", "ischild": True}
WriteJsonValue = json.dumps(MysonInfo)
print(WriteJsonValue)
print(type(WriteJsonValue))