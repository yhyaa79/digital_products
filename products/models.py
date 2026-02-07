from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is enable'), default=True)
    creted_time = models.DateTimeField(_('creted time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)
    
    class Meta():
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    

class Product(models.Model):
    pass


class File(models.Model):
    pass

