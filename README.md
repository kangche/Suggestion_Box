# Suggestion_Box
适用于公司内部的意见箱系统，可以搜集员工的意见发送到指定的邮箱里

# 配置文件
## Suggestion_Box/configure/setting.ini

```[flask11]
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
