from django import forms
from app.models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = {'content', 'email', 'name', 'website'}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholders'] = 'Type your comment...'
        self.fields['email'].widget.attrs['placeholders'] = 'Email'
        self.fields['name'].widget.attrs['placeholders'] = 'Name'
        self.fields['website'].widget.attrs['placeholders'] = 'Website'
