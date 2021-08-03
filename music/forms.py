from django import forms

from .models import MyPlaylist



class MyplayListForm(forms.ModelForm):
    class Meta:
        model = MyPlaylist
        fields = ['mp_title']
        widgets = {
            'mp_title': forms.TextInput(
                attrs={
                    'id': 'mp_title',
                    'placeholder': '재생목록을 입력하세요',
                }
            ),
        }


