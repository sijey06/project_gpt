from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


schema_view = get_schema_view(
   openapi.Info(
      title="GPT Project API",
      default_version='v1',
      description="Документация для приложения GPT Project",
      contact=openapi.Contact(email="sijey06@mail.ru"),
      license=openapi.License(name="License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', 
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]
