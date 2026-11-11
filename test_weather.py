import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Coimbatore,IN&appid=f707220ddf3a6f332e14172848154939&units=metric"

response = requests.get(url)

print(response.status_code)
print(response.text)