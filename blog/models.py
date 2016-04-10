from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#
from tinymce.models import HTMLField

# Create your models here.
#@python_2_unicode_compatible
class Post(models.Model):
    text = HTMLField()
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to="./user_images/", blank=True, null=True)
    postdate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return "%s wrote  %s" % (self.user, self.title)

    def debug(self):
        return "{0}".format(self.__dict__)
