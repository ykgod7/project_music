from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.forms import BaseForm
from django.contrib.auth import authenticate, login


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


class PopupLoginForm(forms.ModelForm):

    def __init__(self,request=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(self.request, username=username, password=password)
            if user is None:
                self.add_error(None, forms.ValidationError('아이디 또는 비밀번호를 확인해주세요'))
            else:
                login(self.request, user)
        return self.cleaned_data




        # try:
        #     user = User.objects.get(username=username)
        #
        #     if not check_password(password, user.password):
        #         self.add_error('password', '비밀번호가 올바르지 않습니다.')
        #     else:
        #         self.user_id = user.id
        # except User.DoesNotExist:
        #     self.add_error('username', '존재하지 않는 아이디 입니다.')
        # return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '아이디를 입력하세요',
                    'id': 'username',
                    'name': 'username',

                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '비밀번호를 입력하세요',
                    'id': 'password',
                    'name': 'password'
                }),
        }
        labels = {
            'username': _('ID'),
            'password': _('PASSWORD')
        }
        help_texts = {
            'username': _(''),
        }

        error_messages = {
            'invalid_login': (
                "비밀번호나 이메일이 올바르지 않습니다. 다시 확인해 주세요."
            ),
            'inactive': ("이 계정은 인증되지 않았습니다. 인증을 먼저 진행해 주세요."),
        }