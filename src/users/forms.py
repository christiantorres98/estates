from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as UserDjango
from django.forms import ModelForm

from users.models import User


class UserDjangoCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserDjangoCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['email'].required = True

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ('document', 'phone', 'role')

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['role'].widget.attrs.update({
            'class': 'form-control select2'
        })
        self.fields['role'].choices = User.ROLE


class UserDjangoModelForm(ModelForm):
    class Meta:
        model = UserDjango
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserDjangoModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
