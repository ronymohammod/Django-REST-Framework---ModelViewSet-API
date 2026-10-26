# from django.urls import path
# from model_viewset.models import *


# path('', BlogAPI.as_view(), name='BlogAPI'),



from django.contrib import admin
from django.urls import path,include

from model_viewset.views import *
from rest_framework.routers import DefaultRouter


route = DefaultRouter()
route.register(r'blog', BlogAPI ,basename='blog')



urlpatterns = [
    path('', include(route.urls)),
]