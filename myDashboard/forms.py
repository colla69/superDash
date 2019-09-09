
from django import forms
from .models import DoneLinksLog, JobsRating


class DoneReading(forms.ModelForm):
    link = forms.CharField(widget=forms.HiddenInput())
    done = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = DoneLinksLog
        fields = ('link', 'done',)


class DoneReading(forms.ModelForm):
    j_id = forms.IntegerField(widget=forms.HiddenInput())
    rating = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = JobsRating
        fields = ('j_id', 'rating',)
