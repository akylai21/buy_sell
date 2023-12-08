from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .serializers import CustomUserCreateSerializer, CustomUserSerializer

from .permissions import IsOwnerOrReadOnly

User = get_user_model()


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer
        return CustomUserSerializer
