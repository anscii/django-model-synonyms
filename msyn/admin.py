from django.contrib import admin
from models import Synonym
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms


class makeSynonymsForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    original = forms.ModelChoiceField(queryset=None, required=False)

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('model').objects.all()
        super(makeSynonymsForm, self).__init__(*args, **kwargs)
        self.fields['original'].queryset = qs



def make_synonyms(modeladmin, request, queryset):

    form = None
    if 'cancel' in request.POST:
        messages.info(request, _(u'Clone deletion cancelled.'))
        return
    elif 'make_synonyms' in request.POST:
        
        try:
            form = makeSynonymsForm(request.POST,model=queryset.model)
        except AttributeError:
            form = modeladmin.makeSynonymsForm(request.POST)


        if form.is_valid():
            original = form.cleaned_data['original']
            objects = queryset.all()
            cnt = len(objects)

            if original is not None:            
                for x in queryset:
                    if x == original:
                        messages.error(request, _(u'Synonyms error: Original should not be in synonyms list.'))
                        return
                cnt+=1 
            
            if cnt > 1:
                ct = ContentType.objects.get_for_model(queryset.model)
                
                for i in range(cnt-1):
                    for j in range(i+1,cnt):
                        if (i == 0) and original is not None:
                            object_id = original.id
                            synonym_id=objects[j-1].id
                        elif original is not None:
                            object_id = objects[i-1].id
                            synonym_id=objects[j-1].id
                        else:
                            object_id = objects[i].id
                            synonym_id=objects[j].id
                        
                        s = Synonym(content_type=ct, object_id=object_id, synonym_id=synonym_id)

                        s.save(force_insert=True)
                
                messages.success(request, _('Synonyms saved.'))                
            else:
                messages.error(request, _("Choose at least 2 synonyms"))

            # self.message_user(request, self.cloneSuccess.render(Context({'count':queryset.count(), 'fics':fics, 'chars':characters})))
            # ct = ContentType.objects.get_for_model(queryset.model)  # for_model --> get_for_model
            # for obj in queryset:
            #     LogEntry.objects.log_action(  # log_entry --> log_action
            #         user_id=request.user.id,
            #         content_type_id=ct.pk,
            #         object_id=obj.pk,
            #         object_repr=obj.title,
            #         action_flag=DELETION,  # actions_flag --> action_flag
            #         change_message=_(u'Clone deleted. Original - ') + original.title)
            return HttpResponseRedirect(request.get_full_path())
    if not form:
        try:
            form = modeladmin.makeSynonymsForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        except AttributeError:
            form = makeSynonymsForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)},model=queryset.model)

    return render_to_response('admin/make_synonyms.html', {'synonyms': queryset, 'form': form, 'path':request.get_full_path()}, context_instance=RequestContext(request))
    
make_synonyms.short_description = _("Mark as synonyms")

class SynonymAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'synonym_object', 'content_type')
    list_display_links = ('content_object',)
    fields = ('content_type', 'object_id', 'synonym_id')
    list_filter = ('content_type',)

admin.site.register(Synonym, SynonymAdmin)
