from django.db import models


class Category(models.Model):
    name = models.CharField('Name of category', max_length=50, null=False, blank=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
