from .utils import ImageGenerator


image_generator = ImageGenerator()


def generate_image_from_prompt(prompt):
    """Сервисная функция для генерации изображения по запросу."""
    return image_generator.generate_image_from_prompt(prompt)


def generate_image_with_template(
        prompt,
        template_file_path
):
    """Сервисная функция для редактирования изображения по шаблону."""
    return image_generator.generate_image_with_template(
        prompt, template_file_path
    )
