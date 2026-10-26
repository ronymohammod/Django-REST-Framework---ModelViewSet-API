
# from django.contrib import admin
# from django.urls import path,include

# from model_viewset.views import *
# from rest_framework.routers import DefaultRouter


# route = DefaultRouter
# route.register(r'blog', BlogAPI ,basename='blog')



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(route.urls)),
# ]



from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('model_viewset.urls')),
]
