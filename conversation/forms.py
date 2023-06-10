from .models import *
from django import forms

class ConversationMessageForm(forms.ModelForm):
    
    class Meta:
        model = ConversationMessage
        fields = ("content",)
        widgets = {
            "content": forms.TextInput(attrs={
                'class':'w-full px-4 py-3 rounded-xl border',
                'rows':'1'
            }),
        }

