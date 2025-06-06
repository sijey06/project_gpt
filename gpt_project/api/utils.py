import os
import base64

import openai
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image

from .constants import IMAGE_SIZE, IMAGE_COUNT


load_dotenv()


class ImageGenerator:
    """Класс для генерации изображений."""

    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = openai.OpenAI(api_key=self.api_key)
        self.image_size = IMAGE_SIZE

    def _convert_image_to_base64(self, img_bytes):
        """Приватный метод преобразования изображения в Base64."""
        with BytesIO() as buffer:
            Image.open(BytesIO(img_bytes)).save(buffer, format='PNG')
            return base64.b64encode(buffer.getvalue()).decode('utf-8')

    def _handle_response(self, response):
        """Приватный метод обработки результата API-запроса."""
        if response.data and len(response.data) > 0:
            return response.data[0].url
        else:
            return 'Изображений не создано.'

    def generate_image_from_prompt(self, prompt: str) -> str:
        """Генерация изображения на основе текстового промта."""
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=IMAGE_COUNT,
                size=self.image_size
            )
            return self._handle_response(response)
        except Exception as e:
            return f'Ошибка: {str(e)}'

    def generate_image_with_template(
            self,
            prompt: str,
            template_img_bytes: bytes
    ) -> str:
        """Создание изображения на основе существующего шаблона."""
        try:
            encoded_image = self._convert_image_to_base64(template_img_bytes)
            response = self.client.images.create_edit(
                image=encoded_image,
                prompt=prompt,
                n=1,
                size=self.image_size
            )
            return self._handle_response(response)
        except Exception as e:
            return f'Ошибка: {str(e)}'
