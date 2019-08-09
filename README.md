## Python学习

## Django学习
```
# 安装Django
pip3 install Django

python3 -m django --version

# 替换掉mysqlclient
pip3 install pymysql
```

错误处理：
```
mysqlclient 1.3.13 or newer is required; you have 0.9.3
```
https://stackoverflow.com/questions/55657752/django-installing-mysqlclient-error-mysqlclient-1-3-13-or-newer-is-required

启动命令：
```
python3 manage.py runserver 8080
```

根据models生成
python3 manage.py makemigrations polls

生成表结构
python3 manage.py sqlmigrate polls 0001

访问链接：
http://127.0.0.1:8000/polls/testdb?aa=345

