from django import forms

class Send_email(forms.form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email
