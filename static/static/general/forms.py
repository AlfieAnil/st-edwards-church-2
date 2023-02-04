from django import forms
member_choices = (
    ("Yes", "Yes"),
    ("No", "No")
)
class ContactUsForm(forms.Form):

    full_name = forms.CharField(max_length=200, 
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    email = forms.CharField(max_length=200, 
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))

    member = forms.ChoiceField(choices=member_choices, 
        widget=forms.Select(attrs={
            'class': 'form-control'
        }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

