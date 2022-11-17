import requests

url = 'http://localhost:5000/upload/'
myfiles = {'file': open('img/teste.txt' ,'rb')}

x = requests.post(url, files = myfiles)

#print the response text (the content of the requested file):

print(x.text)
