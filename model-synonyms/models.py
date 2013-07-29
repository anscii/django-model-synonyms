from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
#from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from managers import SynonymManager


class Synonym(models.Model):
    content_type = models.ForeignKey(ContentType, related_name="synonyms")
    object_id = models.PositiveIntegerField()
    synonym_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    synonym_object = generic.GenericForeignKey()

    synonyms = SynonymManager()

    class Meta:
        verbose_name = _(u'synonym')
        verbose_name_plural = _(u'synonyms')

    def __unicode__(self):
        return u"%s is synonym of %s" % (self.content_object, self.synonym_object)
