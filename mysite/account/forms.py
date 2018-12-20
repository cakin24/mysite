from django import forms
# 引入Django默认的用户模型User类，在这个表的类中就应用User模型，不需要
# 再新建用户数据模型了
from django.contrib.auth.models import User

# 如果提交表单互，不会对数据库进行修改，则继承Form类
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# 如果要将表单中的数据写入数据库表或者修改某些记录的值，就让表单继承ModelForm类
class RegistrationForm(forms.ModelForm):
    # 这两个属性是重新定义的，这里定义了就意味着覆盖或者不需要在内部类Meta中声明数据模型中的字段
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Pssword", widget=forms.PasswordInput)

    class Meta:
        # 声明表单类所应用的数据模型，也就是将来表单的内容会写入到哪个数据库表的哪些记录里面
        model = User
        # 表单类中的属性和数据模型类的属性一一对应
        # 有时我们不必在表单中向数据模型中的所有字段赋值
        # 可以用fields来说明所选用的属性
        fields = ("username", "email")

    # 检验用户所输入的两个密码是否一致，检查动作在调用is_valid（）方法会被执行
    # 以clean_属性名称 命名方式所创建的方法，都有类似功能。
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords do not match.")
        return cd['password2']