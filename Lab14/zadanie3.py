import zadanie2
import requests

api = "https://pbobinski.pythonanywhere.com/post_data"

header = {
    "Authorization": "bb9c093428cc3bc06e3ddc47e460ea5956753e74d54fdcd22ba174bb1e59e516"
}
data = {
    "name": "Kajetan Rosik",
    "url": zadanie2.adres
}

response = requests.post(api, headers=header, json=data)
print(response.text)