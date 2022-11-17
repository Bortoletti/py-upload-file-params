# upload file

curl -F 'img_avatar=@/home/petehouston/hello.txt' http://localhost/upload

curl -F 'img=@/home/luis/usr/VLPR/api/v1001/img/teste.txt' http://localhost:5000/upload

python3 -m pip install flask-cors
python3 -m pip freeze > requirements.txt
