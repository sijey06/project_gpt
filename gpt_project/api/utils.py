import os
import base64
from io import BytesIO
from typing import Union
import openai
from dotenv import load_dotenv
from PIL import Image

from .constants import IMAGE_SIZE, IMAGE_COUNT


load_dotenv()


class ImageGenerator:
    """Класс для генерации изображений."""

    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = openai.OpenAI(api_key=self.api_key)
        self.image_size = IMAGE_SIZE

    def handle_response(self, response):
        """Обрабатывает результат API-запроса."""
        if response.data and len(response.data) > 0:
            return response.data[0].url
        else:
            return 'Изображений не создано.'

    def generate_image_from_prompt(self, prompt):
        """Генерация изображения на основе текстового запроса."""
        try:
            response = self.client.images.generate(
                model="dall-e-2",
                prompt=prompt,
                n=IMAGE_COUNT,
                size=self.image_size
            )
            return self.handle_response(response)
        except Exception as e:
            return f'Ошибка: {str(e)}'

    def generate_image_with_template(self, prompt, template_file_path):
        """Создание изображения на основе существующего шаблона."""
        try:
            with open(template_file_path, "rb") as file:
                response = self.client.images.edit(
                    model="dall-e-2",
                    image=file,
                    prompt=prompt,
                    n=IMAGE_COUNT,
                    size=self.image_size
                )
            return self.handle_response(response)
        except Exception as e:
            return f'Ошибка: {str(e)}'
