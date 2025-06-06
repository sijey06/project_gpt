from django.shortcuts import render
from .forms import ImageGenerationForm
import requests
import json


def simple_generate_image_view(request):
    form = ImageGenerationForm()
    generated_image_url = None
    templates = []  # Будем сохранять полученные шаблоны здесь

    # Отправляем GET-запрос для получения шаблонов
    response_templates = requests.get('http://127.0.0.1:8000/api/template-list/')

    if response_templates.status_code == 200:
        templates = response_templates.json()  # Преобразование JSON в словарь

    if request.method == 'POST':
        form = ImageGenerationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            payload = {
                "prompt": cleaned_data.get('prompt'),
                "app_id": "my-test-app",
                "user_id": "my-test-user"
            }

            response = requests.post(
                'http://127.0.0.1:8000/api/generate-image/',
                headers={'Content-Type': 'application/json'},
                data=json.dumps(payload)
            )

            if response.status_code == 200:
                result = response.json()
                generated_image_url = result.get('image_url')

    context = {
        'form': form,
        'generated_image_url': generated_image_url,
        'templates': templates  # Сюда передаем полученный список шаблонов
    }

    return render(request, 'simple_generate.html', context)
