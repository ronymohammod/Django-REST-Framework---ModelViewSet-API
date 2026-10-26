from model_viewset.serializers import *
from model_viewset.models import *


from rest_framework.viewsets import ModelViewSet


class BlogAPI(ModelViewSet):
    queryset =BlogModel.objects.all()
    serializer_class = BlogSerializer