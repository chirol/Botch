from django import forms
from .models import Recruitment


class RecruitmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['userid'].widget = forms.HiddenInput()

    class Meta:
        model = Recruitment
        fields = ('username', 'userid', 'game', 'area', 'place',
                  'date', 'comment')
