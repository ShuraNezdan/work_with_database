from django.db import models


class Phone(models.Model):
    
    name = models.CharField(max_length=30)
    prise = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
    
    def __str__(self):
        return f'{self.name} - {self.prise}'
