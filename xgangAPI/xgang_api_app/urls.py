from django.urls import path, include
from . import views

from .views import *

from rest_framework import routers

# define the router
router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'xgang', XgangViewSet)
 

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
