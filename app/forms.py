from app.models import *
from django import forms

class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)


class ModelTopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class ModelWebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #widgets={'name':forms.PasswordInput,'url':forms.Textarea}
        labels={'topic_name':'tn','name':'n'}
        help_texts={'name':'this is name'}


class ModelAccessForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'




    
