from django.db import models

## CREDIT
## https://www.youtube.com/watch?v=Drsgp95t-sA
## Master Code Online
## Adding Categories to our blog
# Category model
class Category(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
## END CREDIT


# Product/image model
class Product(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey(Category, default=None)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    originalimage = models.ImageField(upload_to='originalimages')

    def __str__(self):
        return self.name
