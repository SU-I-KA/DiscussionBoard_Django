from django import forms
from .models import *

class NewTopicForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea(attrs=
    {'placeholder': 'type in ypur message',
    'rows':5
    }),
     max_length=4000, help_text='max length is 4000', required=True)
    
    class Meta:
        model = Topic
        fields = ['subject', 'message']