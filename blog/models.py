from __future__ import unicode_literals
import json
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
#@python_2_unicode_compatible
class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to="./user_images/", blank=True, null=True)
    postdate = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return "%s wrote  %s" % (self.user, self.title)

    def debug(self):
        dump = self.__dict__
        return "{0}".format(dump)

    def json(self):
        j = self.__dict__
        u = self.user
        del j['_state']
        del j['postdate']
        del j['_user_cache']
        j['edit_link'] = self.edit_link
        j['delete_link'] = self.delete_link
        j['user'] = {
            'first_name': u.first_name,
            'first_last': u.last_name
        }
        print j
        return j

    @property
    def edit_link(self):
        return reverse('post_edit', args=[self.id])

    def html_edit_link(self):
        return "<a href='{0}' title='edit {1}'><i class='fa fa-pencil-square-o'></i> </a>" \
        .format(self.edit_link,self.title)

    @property
    def delete_link(self):
        return reverse('post_delete', args=[self.id])

    def html_delete_link(self):
        return "<a href='{0}' title='delete {1}'><i class='fa fa-trash'></i> </a>" \
        .format(self.delete_link,self.title)
