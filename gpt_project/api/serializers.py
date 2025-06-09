from rest_framework import serializers

from .models import PromptTemplate


class ImageRequestSerializer(serializers.Serializer):
    """Сериализатор для проверки входящих данных."""

    prompt = serializers.CharField(required=False)
    template_id = serializers.IntegerField(required=False, allow_null=True)
    template_file = serializers.ImageField(required=False, allow_null=True)
    app_id = serializers.CharField(required=True)
    user_id = serializers.CharField(required=True)

    def validate(self, attrs):
        if not attrs.get('template_id') and not attrs.get('prompt'):
            raise serializers.ValidationError(
                'Необходимо выбрать шаблон, либо ввести текст.'
            )
        return attrs


class PromptTemplateSerializer(serializers.ModelSerializer):
    """Сериализатор шаблонов."""

    image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PromptTemplate
        fields = '__all__'

    def get_image_url(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return obj.image.url
        return None
