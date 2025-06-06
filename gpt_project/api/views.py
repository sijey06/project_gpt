from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from .decorators import validate_app_id
from .models import Application, PromptTemplate, Statistics
from .serializers import ImageRequestSerializer, PromptTemplateSerializer
from .services import generate_image_from_prompt, generate_image_with_template


class CreateImageViewSet(CreateModelMixin, GenericViewSet):
    """Представление для обработки POST-запросов на генерацию изображений."""

    serializer_class = ImageRequestSerializer

    @validate_app_id
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        user = request.user
        app_id = kwargs.get('app_id') or validated_data.get('app_id')

        if not isinstance(user, AnonymousUser) and app_id:
            try:
                application = Application.objects.get(app_id=app_id)
                stat, created = Statistics.objects.get_or_create(
                    user=user,
                    app=application
                )
                stat.increment_total_requests()
            except Application.DoesNotExist:
                return Response(
                    {"detail": "Приложение не найдено"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        prompt = (
            PromptTemplate.objects.filter(
                id=validated_data.get('template_id')
            ).first().description
            if validated_data.get('template_id')
            else validated_data.get('prompt')
        )

        image_url = (
            generate_image_with_template(
                prompt, validated_data['template_file'].read()
            )
            if validated_data.get('template_file')
            else generate_image_from_prompt(prompt)
        )

        return Response({'image_url': image_url}, status=status.HTTP_200_OK)


class TemplateListAPI(ReadOnlyModelViewSet):
    queryset = PromptTemplate.objects.all()
    serializer_class = PromptTemplateSerializer
