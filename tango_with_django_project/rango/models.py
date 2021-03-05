from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kargs):
        self.slug = slugify(self.name)
        if self.views < 0: self.views = 0
        super(Category, self).save(*args, **kargs)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    page_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, default='images.jpg')

    def __str__(self):
        return self.user.username