from rest_framework import routers
from .views import *
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('batch',BatchViewSet)


urlpatterns = [
    path('api/',include(router.urls)),
    path('codes_list/', StoreCodesApi.as_view()),
    path('login/',obtain_auth_token)

]
