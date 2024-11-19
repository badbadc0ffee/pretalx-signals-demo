from django.db import models
from pretalx.mail.models import QueuedMail
from pretalx.person.models.user import User
from pretalx.submission.models import Submission


class TechRider(models.Model):
    submission = models.ForeignKey(
        to=Submission,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Tech Rider",
    )


class UserNotes(models.Model):
    person = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    notes = models.TextField()


class MailNotes(models.Model):
    mail = models.ForeignKey(
        to=QueuedMail,
        on_delete=models.CASCADE,
    )
    notes = models.TextField()
