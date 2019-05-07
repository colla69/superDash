
from django import forms
from .models import DoneLinksLog


class DoneReading(forms.ModelForm):
    link = forms.CharField(widget=forms.HiddenInput())
    done = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = DoneLinksLog
        fields = ('link', 'done',)

