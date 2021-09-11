from django import forms

from estates.models import Estate


class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EstateForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
