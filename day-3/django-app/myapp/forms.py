from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title of task", max_length=200)
    description = forms.CharField(label="Description of the area",widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Name of the project", max_length=200)