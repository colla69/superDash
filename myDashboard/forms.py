
from django import forms
from .models import DoneLinksLog, JobsRating


class DoneReading(forms.ModelForm):
    link = forms.CharField(widget=forms.HiddenInput())
    done = forms.BooleanField(widget=forms.HiddenInput())

    class Meta:
        model = DoneLinksLog
        fields = ('link', 'done')


class JobsRatingForm(forms.ModelForm):
    job_id = forms.CharField(widget=forms.HiddenInput())
    rate = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = JobsRating
        fields = ('job_id', 'rate')
