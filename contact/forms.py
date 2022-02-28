from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput
                             (attrs={'placeholder': 'Email'}))
    subject = forms.CharField(max_length=100,
                              required=True, widget=forms.TextInput
                              (attrs={'placeholder': 'subject'}))
    message = forms.CharField(required=True,
                              widget=forms.TextInput
                              (attrs={'placeholder': 'message',
                                      'style': 'width: 300px;', 'style':
                                      'height: 150px;'}))
