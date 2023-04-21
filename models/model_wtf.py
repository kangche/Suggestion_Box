from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, StringField, PasswordField
# from wtforms.validators import DataRequired, EqualTo, Length
from flask_ckeditor import CKEditorField

class Myform(FlaskForm):
    # name = StringField(label='提交人:' ,validators=[DataRequired()])
    name = StringField(label='提交人:')
    submit = SubmitField(label= '提交意见')
    body = CKEditorField('body')

# class Myform1(FlaskForm):

#     name = StringField(label= '你的名字:', 
#                         validators=[DataRequired()], render_kw={'placeholder': '输入域账号'})
#     pwd = PasswordField(label= '密码', 
#                         validators=[DataRequired()], render_kw={'placeholder': '输入当前密码'})
#     pwd_n1 = PasswordField(label= '新密码', 
#                            validators=[DataRequired(), Length(min=8), EqualTo('pwd_n2')], render_kw={'placeholder': '输入新密码'})
#     pwd_n2 = PasswordField(label= '重新输入新密码', 
#                            validators=[DataRequired(), EqualTo('pwd_n1')], render_kw={'placeholder': '重新输入新密码'})
#     submit = SubmitField(label= '提交', validators=[DataRequired()])
    



 