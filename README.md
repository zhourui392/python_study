## Python学习

## Django学习
pip3 install Django

python3 -m django --version

python3 manage.py runserver 8080


pip3 install pymysql
错误处理：
```
mysqlclient 1.3.13 or newer is required; you have 0.9.3
```
https://stackoverflow.com/questions/55657752/django-installing-mysqlclient-error-mysqlclient-1-3-13-or-newer-is-required


根据models生成
python3 manage.py makemigrations polls

生成表结构
python3 manage.py sqlmigrate polls 0001

