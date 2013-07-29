from django.db.models import Manager

from django.contrib.contenttypes.models import ContentType


class SynonymManager(Manager):
    def get_for_object_in_bulk(self, objects):
        objects = list(objects)
        if len(objects) > 0:
            ctype = ContentType.objects.get_for_model(objects[0])
            synonyms = list(self.filter(content_type__pk=ctype.id,
                                        object_id__in=[obj._get_pk_val() for obj in objects]))
            synonym_dict = dict([(synonym.object_id, synonym) for synonym in synonyms])
        else:
            synonym_dict = {}
        return synonym_dict
