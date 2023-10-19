from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

class Photography(models.Model):

    OPTIONS_CATEGORY = [
        ("PORTIFOLIO","Portifolio"),
        ("PROJETOS","Projetos"),
        ("CLT","clt"),
        ("COMUNIDADE","Comunidade"),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=OPTIONS_CATEGORY, default='')
    description = models.TextField(null=False, blank=False)
    path = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    published = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    date_photography = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.name