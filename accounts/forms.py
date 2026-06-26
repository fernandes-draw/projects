

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):

    cargo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Selecione o nível de acesso",
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True
    )

    class Meta():
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name != 'cargo':
                field.widget.attrs['class'] = 'form-control'
