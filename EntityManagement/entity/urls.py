from django.urls import path, include
from entity import views
from entity.views import EntityViewSet, TagViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'api/tags', TagViewSet, basename='tags')
router.register(r'api/entities', EntityViewSet, basename='entities')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'api/discover/', views.discover)
]
