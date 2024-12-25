from django.dispatch import receiver

from pretalx.mail.signals import mail_form_html, mail_forms
from pretalx.person.signals import speaker_form_html, speaker_forms
from pretalx.submission.signals import (
    submission_form_html,
    submission_form_link,
    submission_forms,
)

from .forms import MailNotesForm, TechRiderForm, UserNotesForm
from .models import MailNotes, TechRider, UserNotes


@receiver(speaker_forms)
def speaker_forms(sender, request, person, **kwargs):
    notes, __ = UserNotes.objects.get_or_create(person=person)
    return UserNotesForm(
        instance=notes,
        data=request.POST if request.method == "POST" else None,
        prefix="notes",
    )


@receiver(speaker_form_html)
def test_speaker_form_html(sender, request, user, **kwargs):
    return '<i class="fa fa-coffee mr-2"></i> Demo text below speaker form'


@receiver(submission_forms)
def submission_forms(sender, request, submission, **kwargs):
    tr, __ = TechRider.objects.get_or_create(submission=submission)
    return TechRiderForm(
        instance=tr,
        data=request.POST if request.method == "POST" else None,
        prefix="tech_rider",
    )


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
def mail_forms(sender, request, mail, **kwargs):
    notes, __ = MailNotes.objects.get_or_create(mail=mail)
    return MailNotesForm(
        instance=notes,
        data=request.POST if request.method == "POST" else None,
        prefix="notes",
    )


@receiver(mail_form_html)
def mail_form_html(sender, request, mail, **kwargs):
    return '<i class="fa fa-coffee mr-2"></i> Demo text below mail form'


try:
    from samaware.signals import speaker_html, submission_html

    @receiver(speaker_html)
    def speaker_html(sender, request, user, **kwargs):
        return '<h3>Demo</h3><i class="fa fa-coffee mr-2"></i> Demo text for Speaker'

    @receiver(submission_html)
    def submission_html(sender, request, submission, **kwargs):
        return '<h3>Demo</h3><i class="fa fa-coffee mr-2"></i> Demo text for Submission'

except ImportError:
    pass
