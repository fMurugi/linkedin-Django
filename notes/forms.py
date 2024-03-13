from django import forms
from .models import Notes
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control my-5'}),
            'content':forms.Textarea(attrs={'class':'form-control my-5'}),
        }

        labels = {
            'text': 'Write your note here',
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError('Title is too short')
        return title
