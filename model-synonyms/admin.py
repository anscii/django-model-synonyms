from django.contrib import admin
from models import Synonym


class SynonymAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'synonym_object', 'content_type')
    list_display_links = ('content_object',)

admin.site.register(Synonym, SynonymAdmin)
