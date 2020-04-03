from django.conf.urls import url, include
from django.contrib import admin
from api.resources import UserResource

user_resource = UserResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(user_resource.urls))
]
