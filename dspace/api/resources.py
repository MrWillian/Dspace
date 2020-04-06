from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from api.models import Address

class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'

class AddressResource(ModelResource):
  user = fields.ForeignKey(UserResource, 'user')
  class Meta:
    queryset = Address.objects.all()
    resource_name = 'Address'
