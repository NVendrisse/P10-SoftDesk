from django.db import models
from authentification.models import User
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    class ProjectTypes(models.TextChoices):
        BACKEND = "B", _("Back-end")
        FRONTEND = "F", _("Front-end")
        IOS = "I", _("iOS")
        ANDROID = "A", _("Android")

    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=2048)
    type = models.CharField(max_length=10, choices=ProjectTypes.choices)
    time_created = models.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(
        to=User, through="contributor", related_name="contributor_list", default=[]
    )


class Contributor(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):
    class Priority(models.TextChoices):
        LOW = "L", _("LOW")
        MID = "M", _("MEDIUM")
        HIG = "H", _("HIGH")

    class Nature(models.TextChoices):
        BUG = "B", _("BUG")
        FEA = "F", _("FEATURE")
        TAS = "T", _("TASK")

    class ProgressStatus(models.TextChoices):
        TOD = "T", _("TODO")
        INP = "I", _("IN PROGRESS")
        FIN = "F", _("FINISHED")

    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=1, choices=Priority.choices)
    nature = models.CharField(max_length=1, choices=Nature.choices)
    status = models.CharField(max_length=1, choices=ProgressStatus.choices)
    title = models.CharField(max_length=56)
    description = models.CharField(max_length=1024)
    attributed_user = models.ForeignKey(
        to=User, null=True, on_delete=models.SET_NULL, related_name="attributed"
    )


class Comment(models.Model):
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
    time_created = models.DateTimeField(auto_now_add=True)
