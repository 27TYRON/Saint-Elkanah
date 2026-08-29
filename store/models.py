from django.db import models


class Perfume(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    size = models.CharField(
        max_length=100,
        blank=True
    )

    fragrance_notes = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to='perfumes/'
    )

    is_featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
