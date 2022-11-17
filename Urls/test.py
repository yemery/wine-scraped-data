# [{"name": "Felix Maina", "years": 21, "school": "Makerere"}]import json
# # Data to be written
# details = [{
#         "name": "Felix Maina",
#         "years": 21,
#         "school": "Makerere"
# }]
# # Serializing JSON and writing JSON file
# with open("data.json", "w") as file_object:
#     json.dump(details, file_object)  # {"

wf=open('Urls/Url.txt',"r+")
lines=wf.readlines()
for i in lines:
    print(i.rstrip())