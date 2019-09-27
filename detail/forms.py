from django import forms
from .models import Detail,Comment

class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['title', 'content'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']


        
    
