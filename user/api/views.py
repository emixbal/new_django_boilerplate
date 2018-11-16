from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import detail_route, list_route
from django_filters.rest_framework import DjangoFilterBackend
import requests
from rest_framework_jwt.settings import api_settings
from rest_framework.pagination import LimitOffsetPagination

from ..serializers import UserSerializer
from companies.serializers import CompaniesSerializer

class UserViewset(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    filter_fields = ('username', 'email', 'company_id',)
    search_fields = ('username', 'email',)
    ordering_fields = ('__all__')

    @detail_route(methods=['get'], permission_classes=[IsAuthenticated])
    def companies(self, request, pk=None):
        user = User.objects.get(pk=pk)
        companies = user.companies_set.all()

        serializer = CompaniesSerializer(companies, many=True)
        return Response({
            'count': user.companies_set.count(),
            'results': serializer.data
        }, status.HTTP_200_OK)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
