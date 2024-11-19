from django import forms
from django.dispatch import receiver
from pretalx.mail.signals import mail_form_html, mail_forms
from pretalx.person.signals import speaker_form_html, speaker_forms
from pretalx.submission.signals import (
    submission_form_html,
    submission_form_link,
    submission_forms,
)


class DummyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.prefix = "dummy_prefix"
        super().__init__(*args, **kwargs)

    text = forms.CharField(
        label="Dummy Text",
        initial="Lorem ipsum",
    )

    number = forms.IntegerField(label="Dummy Number", initial=12345, required=False)


@receiver(speaker_forms)
def speaker_forms(sender, **kwargs):
    return DummyForm


@receiver(speaker_form_html)
def test_speaker_form_html(sender, request, user, **kwargs):
    return '<i class="fa fa-coffee mr-2"></i> Demo text below speaker form'


@receiver(submission_forms)
def submission_forms(sender, **kwargs):
    return DummyForm


@receiver(submission_form_html)
def submission_form_html(sender, request, submission, **kwargs):
    return '<i class="fa fa-coffee mr-2"></i> Demo text below submission form'


@receiver(submission_form_link)
def submission_form_link(sender, request, submission, **kwargs):
    return """<a href="#" class="dropdown-item" role="menuitem">
            <i class="fa fa-coffee"></i>
            Demo link
        </a>"""


@receiver(mail_forms)
def mail_forms(sender, **kwargs):
    return DummyForm


@receiver(mail_form_html)
def mail_form_html(sender, request, mail, **kwargs):
    return '<i class="fa fa-coffee mr-2"></i> Demo text below mail form'
