from django import forms

from .models import MailNotes, TechRider, UserNotes


class TechRiderForm(forms.ModelForm):
    class Meta:
        model = TechRider
        exclude = ["submission"]


class UserNotesForm(forms.ModelForm):
    class Meta:
        model = UserNotes
        exclude = ["person"]


class MailNotesForm(forms.ModelForm):
    class Meta:
        model = MailNotes
        exclude = ["mail"]
