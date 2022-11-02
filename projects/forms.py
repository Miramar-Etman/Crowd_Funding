from django import forms
from .models import Project, Donate, Comment, Rating

################# Create Project Form ######################
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'start_date','end_date', 'Category','images','target','tags']

##################### Donations Form #######################
class DonateForm(forms.ModelForm):
        class Meta:
            model = Donate
            fields = ['amount']

##################### Commenting Form #########################
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']

##################### Rating Project Form ####################
class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['scale']

######################## Reporting Project Form ###################
class ReportProjectForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['scale']