import requests


domain = input("Enter the domain : ")
url = f"https://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=text&fl=original&collapse=urlkey"
data = requests.get(url)
print(data.text)
