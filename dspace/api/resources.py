from django.contrib.auth.models import User
from api.models import Address
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields

class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'
    authorization = Authorization()

class AddressResource(ModelResource):
  user = fields.ToOneField(UserResource, 'user', null=True, blank=True)

  class Meta:
    queryset = Address.objects.all()
    resource_name = 'address'
    authorization = Authorization()
