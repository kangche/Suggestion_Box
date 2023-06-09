from flask import Blueprint, render_template, request, url_for, flash, redirect, abort, current_app
from models.model_wtf import Myform
from models.model_sendmail import send_mail
from models.model_logger import custom_logger


noauth = Blueprint('noauth', __name__)



@noauth.route('/', methods=['GET', 'POST'])
def test1():
    form = Myform()
    if request.method == 'POST' and form.validate_on_submit():
        message = form.body.data
        name = form.name.data
        if not message:
            flash('要提交的内容不能为空', 'error')
            return render_template('input2.html',form = form)
        if not name:
            flash('如果实名提交意见，提交人处不能为空。', 'error')
            return render_template('input2.html',form = form)

        try:
            send_mail('<h1>意见来自: {name}</h1><br><br>'.format(name=name)+message)
            flash('意见提交成功', 'info')
            custom_logger.info(f"客户端IP：{request.remote_addr}内容：{str(message)}结果：'success'")
            return redirect(url_for('noauth.result'))
        except Exception  as e:
            flash('意见提交失败请联系IT', 'error')
            custom_logger.error(f"客户端IP：{request.remote_addr} 内容：{str(message)} 结果：'fail'")
            return render_template('input2.html',form = form)
    return render_template('input2.html', form = form)

@noauth.route('/result', methods=['GET'])
def result():
    if request.referrer == request.url_root:
        return render_template('input3.html'), {"Refresh": "2; url=/"}
    else:
        abort(404)

 