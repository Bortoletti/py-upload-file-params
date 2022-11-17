import requests
import json

url = 'http://localhost:5000/upload/'
myfiles = {'file': open('img/teste.txt' ,'rb')}

params = json.loads(  '{"nome":"luis"}' )
#print( params['nome'])

y = requests.post(url, json= params )
print( y.text )

x = requests.post(url, files = myfiles)
print(x.text)

z = requests.post(url, files = myfiles, json= params )
print(z.text)
