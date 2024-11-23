#django-nextjs-backend-api\src\waitlists\forms.py

from django import forms
from django.utils import timezone
from .models import WaitlistEntry

class WaitlistEntryCreateForm(forms.ModelForm):
    class Meta:
        #email = forms.EmailField( - another way to declare)
        model = WaitlistEntry
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        today = timezone.now().day
        qs = WaitlistEntry.objects.filter(
            email=email,
            timestamp__day=today)
        #if qs.exists():
        if qs.count() >=5:
            raise forms.ValidationError("Cannot enter this email Again today.")
       # if email.endswith('@gmail.com'):
        #    raise forms.ValidationError('cannot use gmail')
        return email
