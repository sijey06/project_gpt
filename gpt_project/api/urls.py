from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CreateImageViewSet, TemplateListAPI


router = DefaultRouter()
router.register(
    r'generate-image', CreateImageViewSet, basename='generate-image'
)
router.register(r'templates', TemplateListAPI, basename='templates')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('get-token/', views.obtain_auth_token),
]
