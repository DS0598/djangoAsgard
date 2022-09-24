from django.db import models


class Asgard(models.Model):
    title = models.CharField(max_length=700)
    description = models.CharField(max_length=700)

    def __str__(self):
        return self.title
