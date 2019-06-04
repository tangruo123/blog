from django import forms
from .models import User, Comment

# 注册表单
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",
                                                             "class": "form-control", }),
                              max_length=50,error_messages={"required": "username不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email", "required": "required",
                                                           "class": "form-control", }),
                              max_length=50,error_messages={"required": "email不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",
                                                                 "class": "form-control", }),
                               max_length=20, error_messages={"required": "password不能为空", })

    '''
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    '''

# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "required": "required",
                                                             "class": "form-control", }),
                               max_length=50, error_messages={"required": "username不能为空", })
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "required": "required",
                                                                 "class": "form-control", }),
                               max_length=20, error_messages={"required": "password不能为空", })
# 评论表单
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']