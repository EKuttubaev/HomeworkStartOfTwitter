from django.contrib.auth.models import User
from django.db.models import Model
from django.db import models


class Tweet(Model):
    text = models.CharField(verbose_name="Текст", max_length=250)
    created_date = models.DateField(verbose_name="Дата создания", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Автор",on_delete=models.CASCADE,)
    likes = models.IntegerField(verbose_name="Количество лайков", default=0)

    def __str__(self):
        return self.text

