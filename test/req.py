import requests

data=requests.get("https://api.sorare.com/graphql")
print(data.status_code)