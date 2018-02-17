from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    
    class Meta: # to dell django which model be used to create
        model =Post
        fields =('title','text')

