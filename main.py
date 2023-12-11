
import requests


url_get = 'https://httpbin.org/get'
print('GET запрос')
req = requests.get(url_get)
print(f"Код: {req.status_code} \nЗаголовки: {req.headers} \nТело: {req.text} ")


url_post = 'https://httpbin.org/post'
print('POST запрос')
req = requests.post(url_post)
print(f"Код: {req.status_code} \nЗаголовки: {req.headers} \nТело: {req.text} ")


print('OPTIONS запрос')
req = requests.options(url_post)
print(f"Код: {req.status_code} \nЗаголовки: {req.headers} \nТело: {req.text} ")
print(f"Разрешённые методы: {req.headers['Allow']}")
