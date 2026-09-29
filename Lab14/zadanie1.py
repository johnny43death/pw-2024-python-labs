import requests

url = 'https://pbobinski.pythonanywhere.com/get_api_key?user=337375'
klucz = requests.get(url)
print(klucz.json())

# bb9c093428cc3bc06e3ddc47e460ea5956753e74d54fdcd22ba174bb1e59e516