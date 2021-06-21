from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.TextField()
    price = models.FloatField()
    image = models.FileField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField()
