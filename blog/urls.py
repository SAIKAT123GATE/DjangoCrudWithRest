from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
# router.register(r'apioverview', views.ApiOverview)
urlpatterns = [

    # path('apioverview', views.ApiOverview, name="home"),
    path('', include(router.urls))
]
