from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from rest_framework.viewsets import ModelViewSet

from api.v1.schemas import (
    TOKEN_OBTAIN_SCHEMA, TOKEN_REFRESH_SCHEMA,
    USER_VIEW_SCHEMA, USER_ME_SCHEMA,
)
from api.v1.permissions import IsOwnerPut
from api.v1.serializers import UserRegisterSerializer, UserUpdateSerializer
from user.models import User


@extend_schema(**TOKEN_OBTAIN_SCHEMA)
class TokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(**TOKEN_REFRESH_SCHEMA)
class TokenRefreshView(TokenRefreshView):
    pass


@extend_schema_view(**USER_VIEW_SCHEMA)
class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    http_method_names = ('get', 'post', 'put',)

    @extend_schema(exclude=True)
    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed(request.method)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserRegisterSerializer
        return UserUpdateSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
        if self.request.method == 'PUT':
            self.permission_classes = (IsOwnerPut,)
        return super().get_permissions()

    @extend_schema(**USER_ME_SCHEMA)
    @action(detail=False,
            methods=('get',),
            url_path='me',
            url_name='users-me',
            )
    def me(self, request):
        instance: User = request.user
        serializer = UserUpdateSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
