from django.urls import path
from .views import (
    home,
    list_templates,
    generate_image,
    register,
    login_view,
    logout_view,
    select_template
)


urlpatterns = [
    path('', home, name='home'),
    path('list-templates/', list_templates, name='list_templates'),
    path('generate-image/', generate_image, name='generate_image'),
    path(
        'templates/<int:template_id>/',
        select_template,
        name='select_template'
    ),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
