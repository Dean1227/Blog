
from django import forms


class MessageForm(forms.Form):

    name = forms.CharField(max_length=10, required=True,
                               error_messages={'required': '昵称必填',
                                               'max_length': '最大长度为10'})

    email = forms.CharField(required=True, error_messages={'required': '邮箱必填'})

    lytext = forms.CharField(required=True, error_messages={'required': '内容必填'})


    # def clean(self):
    #     # 校验用户名是否已经注册
    #     name = self.cleaned_data.get('name')
    #     if not name:
    #         raise forms.ValidationError({'name': '昵称必填'})
    #     email = self.cleaned_data.get('name')
    #     if not email:
    #         raise forms.ValidationError({'email': '邮箱必填'})
    #     lytext = self.cleaned_data.get('lytext')
    #     if not lytext:
    #         raise forms.ValidationError({'content': '内容必填'})
    #     return self.cleaned_data