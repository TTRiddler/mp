from django import forms
from feedback.models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('name', 'email', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control px-0 font-2 inp', 'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control px-0 font-2 inp', 'placeholder': 'Ваш е-mail для связи'}),
            'text': forms.Textarea(attrs={'class': 'form-control px-0 font-2 inp', 'placeholder': 'Ваше сообщение', 'rows': 5}),
        }