from django import forms
from .models import Recruitment


class RecruitmentForm(forms.ModelForm):

    class Meta:
        model = Recruitment
        fields = '__all__'