from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='images_created',
                            on_delete=models.CASCADE)
    #many-to-many relationship
    users_like=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)                        
    title=models.CharField(max_length=200)                        
    slug=models.SlugField(max_length=200, blank=True)
    url=models.URLField()
    image=models.ImageField(upload_to='images/%Y/%m/%d/')
    description=models.TextField(blank=True)
    created=models.DateField(auto_now_add=True, db_index=True)
    #use db_index=True so that Django
    #creates an index in the database for this field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.title
# Create your models here.
"""
Database indexes improve query performance. Consider setting
db_index=True for fields that you frequently query using
filter(), exclude(), or order_by(). ForeignKey fields or
fields with unique=True imply the creation of an index. You can
also use Meta.index_together or Meta.indexes to create
indexes for multiple fields. You can learn more about database
indexes at https://docs.djangoproject.com/en/3.0/ref/
models/options/#django.db.models.Options.indexes.
"""


#The
#ManyToManyField fields provide a many-to-many manager that allows you to
#retrieve related objects, such as image.users_like.all() , or get them from
#a user object, such as user.images_liked.all() .