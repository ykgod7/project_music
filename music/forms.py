from django import forms
from django.contrib.auth.hashers import check_password  # 패스워드 비교용
from .models import MyPlaylist, PlaylistComment
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="아이디", max_length=32,
                               error_messages={'required': "아이디를 입력하세요"})
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput,
                               error_messages={'required': "비밀번호를 입력하세요"})

class MyplayListForm(forms.ModelForm):
    class Meta:
        model = MyPlaylist
        fields = ['mp_name']
        widgets = {
            'mp_name': forms.TextInput(
                attrs={
                    'id': 'mp_name',
                    'placeholder': '재생목록을 입력하세요',
                }
            ),
        }
