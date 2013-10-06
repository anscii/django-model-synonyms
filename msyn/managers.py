from django.db.models import Manager

from django.contrib.contenttypes.models import ContentType


class SynonymManager(Manager):
    def get_for_objects(self, objects):
        objects = list(objects)
        if len(objects) > 0:
            ctype = ContentType.objects.get_for_model(objects[0])
            synonyms = list(self.filter(content_type__pk=ctype.id,
                                        object_id__in=[obj._get_pk_val() for obj in objects]))
            synonym_dict = dict([(synonym.object_id, synonym) for synonym in synonyms])
        else:
            synonym_dict = {}
        return synonym_dict


    def get_for_object(self, object):
        ctype = ContentType.objects.get_for_model(object)
        from django.db.models import Q

        object_id = object._get_pk_val()

        synonyms = self.filter(Q(content_type__pk=ctype.id) & (Q(object_id=object_id) | Q(synonym_id=object_id) ) )

        for syn in synonyms:
            if syn.synonym_id == object_id:
                syn.reverse = True            

        # synonyms = self.filter(content_type__pk=ctype.id,
        #                                 object_id=object._get_pk_val())

        return synonyms

