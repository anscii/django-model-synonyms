from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
#from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from managers import SynonymManager


class Synonym(models.Model):
    #CHOICES =  {"model__in": ("author", "tag")}
    try:
        CHOICES = {"model__in": settings.MSYN_CONTENT_TYPES_LIMIT }
    except NameError, e:
        CHOICES =  {}


    content_type = models.ForeignKey(ContentType, limit_choices_to = CHOICES, related_name="synonyms")
    object_id = models.PositiveIntegerField(db_index=True)
    synonym_id = models.PositiveIntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    synonym_object = generic.GenericForeignKey('content_type', 'synonym_id')

    synonyms = SynonymManager()

    _reverse = False


    class Meta:
        verbose_name = _(u'synonym')
        verbose_name_plural = _(u'synonyms')

    def __unicode__(self):
        return u"%s is synonym of %s" % (self.content_object, self.synonym_object)
    
    @property
    def reverse(self):
        if self._reverse is not None and self._reverse:
            return True
        else:
            return False
        # return self._reverse

    @reverse.setter
    def reverse(self, value):        
        self._reverse = value

    @property
    def synonym(self):
        if not self.reverse:
            return self.synonym_object
        else:
            return self.content_object

    @property
    def object(self):
        if not self.reverse:
            return self.content_object
        else:
            return self.synonym_object


