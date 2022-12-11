from django.contrib.auth.models import User

from tastypie.resources import ModelResource
from .models import Entry
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication, Authentication
from tastypie.authorization import Authorization, DjangoAuthorization
import pdb
from tastypie.constants import ALL, ALL_WITH_RELATIONS


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authentication = Authentication()
        authorization = Authorization()
        resource_uri = False
    


class EntryResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user', full=True)

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        authentication = Authentication()
        authorization = Authorization()
        resource_uri = False
        filtering = {
            "slug": ('exact', 'startswith',),
            "title": ALL,
        }

    def obj_get_list(self, bundle, **kwargs):
        return Entry.objects.all()

    def obj_get(self, bundle, **kwargs):
        print(bundle.request.user)
        return Entry.objects.get(id=kwargs['pk'])

    
    # def dehydrate_title(self, bundle):
    #     # print(bundle)
    #     # print(bundle.data)
    #     # print(bundle.obj.slug)
    #     return bundle.data['title'].upper()

    # def hydrate_slug(self, bundle):
    #     bundle.obj.slug = bundle.data['title']
    #     bundle.obj.save()
    #     print(bundle.obj.slug)
    #     return bundle
    

