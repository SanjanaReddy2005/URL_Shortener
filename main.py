import requests

def shorten_link(full_link,link_name):
     API_KEY = 'a875b8af1135cdaf8eaea992f77ef3af9ac32'
     # BASE_URL = ''
     BASE_URL = 'https://cutt.ly/api/api.php'

     payload = {'key': API_KEY, 'short': full_link, 'name':link_name}
     request = requests.get(BASE_URL, params=payload)
     data = request.json()

     print(data)


shorten_link(input('Enter the url which you want to shorten it :'),input('Enter the name which you want to give it :'))
