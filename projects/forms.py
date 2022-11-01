from django import forms
from .models import Project, Donate, Comment, Rating


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'start_date','end_date', 'Category','images','target','tags']

class DonateForm(forms.ModelForm):
        class Meta:
            model = Donate
            fields = ['amount']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['scale']