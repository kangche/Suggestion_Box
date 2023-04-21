# Suggestion_Box
适用于公司内部的意见箱系统，可以搜集员工的意见发送到指定的邮箱里

# 配置文件
## Suggestion_Box/configure/setting.ini

```
[flask11]
apikey = nibawobizuoge   #api key请妥善保管
ckeditor_pkg = full      #ckeditor编辑器样式
ckeditor_height = 400    #ckeditor编辑器的高度

[mail]

smtp_server = mail.zillion.com  #意见通过此地址发出
smtp_port = 25
login_mail = you@mail.com #意见通过此邮箱发出
login_user = you name  #意见通过此邮箱用户发出
login_pass = youpassword #邮箱密码
subject = 意见反馈 # 邮件标题
to = example1@mail.con,example1@mail.con  #意见发到的邮箱可写多个用，隔开
[global]

root_path = '/root/Suggestion_Box #docker部署默认即可，如单机运行则需要改为实际路径'```

## Suggestion_Box/configure/gunicorn.conf.py

gunicorn配置参数

bind = '0.0.0.0:82'  #应用监听地址和端口
workers = '16'
threads = '2'
worker_class = 'sync'
```

# 运行方法
## 本地运行
建议python版本3.10及以上。
```
pip3 install -r requirements.txt
```
```
gunicorn -c configure/gunicorn.conf.py run:app
```
浏览器访问82端口验证是否正常运行。如http://you.server.ip:82
## docker运行
首先在linux机器上安装好docker。
```
docker build -t webapp:v1 .
```
```
docker run -d -p 88:82 webapp:v1
```
浏览器访问88端口验证是否正常运行。如http://you.server.ip:88
