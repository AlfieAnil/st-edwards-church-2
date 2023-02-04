from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from general.models import SacramentContent, PriestMessage
from django import forms
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field
from django_ckeditor_5.widgets import CKEditor5Widget

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsletterUploadForm(forms.Form):
    pdf_file = forms.FileField()



class SacramentEdit(forms.ModelForm):
    # description = RichTextUploadingField()
    class Meta:
        model = SacramentContent
        fields = ['SacramentDescription']

class EditPostForm(forms.ModelForm):
    class Meta:
        model = PriestMessage
        fields = ['Title', 'Message']
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'Message': forms.Textarea(attrs={'class': 'form-control'})
        }