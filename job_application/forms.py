from django import forms

class ContactForm(forms.Form):
    # Specify the name & datatype of the columns here
    # this is for the Form (Webpage)
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)

