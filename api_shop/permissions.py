from .serializers import *
from rest_framework import viewsets

class ClothrsViewSet(viewsets.ModelViewSet):
    serializer_class = ClothesSerializer  # укажи свой сериализатор
    queryset = Clothrs.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
