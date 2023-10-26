from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from api.v1.views import (
    CityView, CurrencyView, ExperienceView, SkillSearchView, SkillCategoryView,
    TaskViewSet, TokenObtainPairView, TokenRefreshView, UserViewSet,
    VacancyViewSet,
)

router = DefaultRouter()

ROUTER_DATA: list[dict[str, ModelViewSet]] = [
    {'prefix': 'tasks', 'viewset': TaskViewSet},
    {'prefix': 'users', 'viewset': UserViewSet},
    {'prefix': 'vacancies', 'viewset': VacancyViewSet},
]

for route in ROUTER_DATA:
    router.register(
        prefix=route.get('prefix'),
        viewset=route.get('viewset'),
        basename=route.get('prefix'),
    )

views: list[path] = [
    path('cities/', CityView.as_view(), name='city'),
    path('currencies/', CurrencyView.as_view(), name='currencies'),
    path('experiences/', ExperienceView.as_view(), name='experiences'),
    path('skills/', SkillSearchView.as_view(), name='skills-search'),
    path('skills/by-categories/', SkillCategoryView.as_view(), name='skill-categories')  # noqa (E501)
]

auth_token: list[path] = [
    path('create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

schema: list[path] = [
    path('', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
]

urlpatterns: list[path] = [
    path('auth/token/', include(auth_token)),
    path('schema/', include(schema)),
    path('', include(router.urls)),
    path('', include(views)),
]
