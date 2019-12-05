from django import forms
from .models import Recruitment


class RecruitmentForm(forms.ModelForm):

    class Meta:
        model = Recruitment
        fields = ('username', 'userid', 'game', 'number', 'area', 'place',
                  'date', 'comment')
        widgets = {
            'date': forms.SelectDateWidget
        }

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['userid'].widget = forms.HiddenInput()
    """
