import requests
response = requests.get("https://raw.githubusercontent.com/Leen-Alzebdeh/lab1/master/print_version.py")
print(response.text)
