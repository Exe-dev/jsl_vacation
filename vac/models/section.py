from django.db import models


class Section(models.Model):
    name = models.CharField('所属名', max_length=255, blank=True, null=True)
    order = models.IntegerField('ソート順', blank=True, null=True)

    def __str__(self):
        return self.name

