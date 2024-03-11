from django.db import models


class Fruits(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name='название'
    )
    price = models.IntegerField(
        verbose_name='цена'
    )

    def __str__(self):
        return self.title
