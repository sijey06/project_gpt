from .utils import ImageGenerator


image_generator = ImageGenerator()


def generate_image_from_prompt(prompt: str) -> str:
    """Сервисная функция для генерации изображения по запросу."""
    return image_generator.generate_image_from_prompt(prompt)


def generate_image_with_template(
        prompt: str,
        template_img_bytes: str
) -> str:
    """Сервисная функция для редактирования изображения по шаблону."""
    return image_generator.generate_image_with_template(
        prompt, template_img_bytes
    )
