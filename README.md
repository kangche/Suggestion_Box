# Suggestion_Box
适用于公司内部的意见箱系统，可以搜集员工的意见发送到指定的邮箱里

# 配置文件
## Suggestion_Box/configure/setting.ini

```[flask11]
apikey = nibawobizuoge
ckeditor_pkg = full
ckeditor_height = 400

[mail]

smtp_server = mail.zillion.com
smtp_port = 25
login_mail = you@mail.com
login_user = you name
login_pass = youpassword
subject = 意见反馈
to = example1@mail.con,example1@mail.con

[global]

root_path = '/root/Suggestion_Box'```
