from django.dispatch import receiver
from pretalx.mail.signals import html_after_mail_badge, html_below_mail_subject
from pretalx.person.signals import html_above_person_form, html_below_person_form
from pretalx.submission.signals import (
    html_above_submission_form,
    html_below_submission_form,
    html_below_submission_link,
)


@receiver(html_above_person_form)
def html_above_person_form(sender, request, user, **kwargs):
    return """<div class="alert alert-warning offset-md-3">
            <span>
                <h5>
                    Demo
                </h5>
                demo for a warning alert above a speaker form
            </span>
        </div>
        <div class="form-group row">
            <label class="col-md-3 col-form-label">
                Demo
            </label>
            <div class="col-md-9">
                <div class="pt-2">
                    demo for an additional form row above a speaker form
                </div>
            </div>
        </div>"""


@receiver(html_below_person_form)
def test_html_below_person_form(sender, request, user, **kwargs):
    return """<div class="alert alert-info">
            <span>
                <h5>
                    Demo
                </h5>
                demo for an info alert below a speaker form
            </span>
        </div>"""


@receiver(html_above_submission_form)
def html_above_submission_form(sender, request, submission, **kwargs):
    return """<div class="alert alert-danger offset-md-3">
            <span>
                <h5>
                    Demo
                </h5>
                demo for a danger alert above a submission form
            </span>
        </div>
        <div class="form-group row">
            <label class="col-md-3 col-form-label">
                Demo
            </label>
            <div class="col-md-9">
                <div class="pt-2">
                    demo for an additional form row above a submission form
                </div>
            </div>
        </div>"""


@receiver(html_below_submission_form)
def html_below_submission_form(sender, request, submission, **kwargs):
    return """<div class="alert alert-info">
            <span>
                <h5>
                    Demo
                </h5>
                demo for an info alert below a submission form
            </span>
        </div>"""


@receiver(html_below_submission_link)
def html_below_submission_link(sender, request, submission, **kwargs):
    return """<a href="#" class="dropdown-item" role="menuitem">
            <i class="fa fa-coffee"></i>
            Demo link
        </a>"""


@receiver(html_after_mail_badge)
def html_after_mail_badge(sender, request, mail, **kwargs):
    return """<i class="fa fa-coffee" title="Demo icon"></i>
        <span class="badge color-info">Demo badge</span>"""


@receiver(html_below_mail_subject)
def html_below_mail_subject(sender, request, mail, **kwargs):
    return """<span class="mb-2 mt-2">
            <i class="fa fa-coffee mr-2"></i>
            Demo text below mail subject
        </span>"""
