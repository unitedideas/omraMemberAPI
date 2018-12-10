from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('memberdata', views.MemberDataView)
urlpatterns = [
    # path('', views.home, name='home'),
    path('', include(router.urls))
]