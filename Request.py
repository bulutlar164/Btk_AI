import requests

url = 'http://localhost:5000/upload-image'
files = {'file': open('image_56.jpg', 'rb')}
response = requests.post(url, files=files)

print(response.json())
