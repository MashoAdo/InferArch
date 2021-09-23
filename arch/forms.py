from django import forms
from django.forms import ModelForm
from .models import Contact

#Contact form for contact page
class ContactForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-group form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'class':'form-group form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject','class':'form-group form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message','class':'form-group form-control'}))
 
    class Meta:
        model = Contact
        fields = '__all__'