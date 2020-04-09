from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from api.resources import UserResource, AddressResource
from api.controllers.calculate import distance

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(AddressResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    url(r'^api/v1/distance/(?P<lat1>\d+\.\d+)/(?P<lon1>\d+\.\d+)/(?P<lat2>\d+\.\d+)/(?P<lon2>\d+\.\d+)$', distance)
]
