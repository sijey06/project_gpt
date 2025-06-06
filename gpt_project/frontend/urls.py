from django.urls import path
from .views import simple_generate_image_view


urlpatterns = [
    path('simple-generate/', simple_generate_image_view, name='simple_generate'),
]
