class Post:
    pass
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()
for i in data:
    if i["id"] == 1:
        print(i["title"])