from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('riderdata', views.RiderView)
urlpatterns = [
    path('member/', views.member, name='member'),
    path('memberform/', views.memberform, name='memberform'),
    path('', include(router.urls))
]
