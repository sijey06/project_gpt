from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Application


def validate_app_id(func):
    def inner_function(*args, **kwargs):
        request = args[1]
        app_id = request.data.get('app_id')

        if not app_id:
            return JsonResponse(
                {'message': 'Требуется указать app_id'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            get_object_or_404(Application, app_id=app_id)
        except Http404:
            return JsonResponse(
                {'message': 'Вашему приложению отказано в доступе.'},
                status=status.HTTP_404_NOT_FOUND
            )

        return func(*args, **kwargs)

    return inner_function
