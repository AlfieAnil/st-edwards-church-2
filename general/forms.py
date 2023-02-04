from django import forms
from general.models import BaptismForm, ChildClass, NewsletterPDF
member_choices = (
    ("Yes", "Yes"),
    ("No", "No")
)

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female")
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


class baptismsForm(forms.ModelForm):
    class Meta:
        model = BaptismForm
        fields = ['practicing_church_time', 'child_surname', 'child_dob', 'child_baptism_name', 'address', 'postcode', 'telephone_number', 'email', 'father_name', 'father_dob', 'father_religion', 'father_baptised_in_parish', 'father_date_baptism', 'father_baptism_church', 'father_date_confirmation', 'father_confirmation_church', 'mother_name', 'mother_dob', 'mother_religion', 'mother_baptised_in_parish', 'mother_date_baptism', 'mother_baptism_church', 'mother_date_confirmation', 'mother_confirmation_church', 'mother_maidan_name', 'parents_marital_status', 'godparent_name_1', 'godparent_religion_1', 'godparent_address_1', 'godparent_postcode_1', 'godparent_telephone_1', 'godparent_dob_1', 'godparent_baptism_church_1', 'godparent_confirmation_date_1', 'godparent_confirmation_church_1', 'godparent_practicing_1', 'godparent_name_2', 'godparent_religion_2', 'godparent_address_2', 'godparent_postcode_2', 'godparent_telephone_2', 'godparent_dob_2', 'godparent_baptism_church_2', 'godparent_confirmation_date_2', 'godparent_confirmation_church_2', 'godparent_practicing_2', 'cw_name', 'cw_gender', 'cw_religion', 'cw_practicing', 'cw_name_2', 'cw_gender_2', 'cw_religion_2', 'cw_practicing_2', 'first_child', 'course_attended', 'course_church']
        widgets = {
            'practicing_church_time': forms.TextInput(attrs={'class': 'form-control'}),
            'child_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'child_dob': forms.DateInput(attrs={'type': 'date'}),
            'child_baptism_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_dob': forms.DateInput(attrs={'type': 'date'}),
            'father_religion': forms.TextInput(attrs={'class': 'form-control'}),
            'father_baptised_in_parish': forms.Select(choices=member_choices, attrs={'class': 'form-control', 'onchange': 'fatherBaptisedChoice()'}),
            'father_date_baptism': forms.DateInput(attrs={'type': 'date'}),
            'father_baptism_church': forms.TextInput(attrs={'class': 'form-control'}),
            'father_date_confirmation': forms.DateInput(attrs={'type': 'date'}),
            'father_confirmation_church': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_dob': forms.DateInput(attrs={'type': 'date'}),
            'mother_religion': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_baptised_in_parish': forms.Select(choices=member_choices, attrs={'class': 'form-control'}),
            'mother_date_baptism': forms.DateInput(attrs={'type': 'date'}),
            'mother_baptism_church': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_date_confirmation': forms.DateInput(attrs={'type': 'date'}),
            'mother_confirmation_church': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_maidan_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parents_marital_status': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_name_1': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_religion_1': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_address_1': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_postcode_1': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_telephone_1': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_dob_1': forms.DateInput(attrs={'type': 'date'}),
            'godparent_baptism_church_1': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_confirmation_date_1': forms.DateInput(attrs={'type': 'date'}),
            'godparent_confirmation_church_1': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_practicing_1': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_name_2': forms.TextInput(attrs={'class': 'form-control', 'onchange': 'secondGodparent()'}),
            'godparent_religion_2': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_postcode_2': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_telephone_2': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_dob_2': forms.DateInput(attrs={'type': 'date'}),
            'godparent_baptism_church_2': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_confirmation_date_2': forms.DateInput(attrs={'type': 'date'}),
            'godparent_confirmation_church_2': forms.TextInput(attrs={'class': 'form-control'}),
            'godparent_practicing_2': forms.TextInput(attrs={'class': 'form-control'}),
            'cw_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cw_gender': forms.Select(choices=gender_choices, attrs={'class': 'form-control'}),
            'cw_religion': forms.TextInput(attrs={'class': 'form-control'}),
            'cw_practicing': forms.TextInput(attrs={'class': 'form-control'}),
            'cw_name_2': forms.TextInput(attrs={'class': 'form-control'}),
            'cw_gender_2': forms.Select(choices=gender_choices, attrs={'class': 'form-control'}),
            'cw_religion_2': forms.TextInput(attrs={'class': 'form-control'}),
            'cw_practicing_2': forms.TextInput(attrs={'class': 'form-control'}),
            'first_child': forms.Select(choices=member_choices, attrs={'class': 'form-control', 'id': 'children-number-selector', 'onchange': 'childrenRows()'}),
            'course_attended': forms.Select(choices=member_choices, attrs={'class': 'form-control'}),
            'course_church': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ChildForm(forms.ModelForm):
    class Meta:
        model = ChildClass
        fields = ['child_name', 'child_dob', 'child_date_baptism', 'child_school']

        widgets = {
            'child_name': forms.TextInput(attrs={'class': 'form-control'}),
            'child_dob': forms.DateInput(attrs={'type': 'date'}),
            'child_date_baptism': forms.DateInput(attrs={'type': 'date'}),
            'child_school': forms.TextInput(attrs={'class': 'form-control'})
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterPDF
        fields = ['newsletter_pdf']