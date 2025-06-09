from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login as auth_user_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings
import requests

from gpt_project.settings import AUTH_TOKEN


def register(request):
    """Обработчик регистрации пользователей."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_user_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'frontend/register.html', {'form': form})


def login_view(request):
    """Авторизация пользователя."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_user_login(request, user)
            return redirect('home')
        else:
            return render(
                request,
                'frontend/login.html',
                {'error': 'Неверные имя пользователя или пароль'}
            )
    return render(request, 'frontend/login.html')


def logout_view(request):
    """Разлогинивание пользователя."""
    auth_logout(request)
    return redirect('home')


def home(request):
    """Главная страница приложения."""
    return render(request, 'frontend/index.html', {})


def list_templates(request):
    """Отображение списка шаблонов."""
    if not request.user.is_authenticated:
        return redirect('login')

    headers = {"Authorization": AUTH_TOKEN}

    response = requests.get(f"{settings.API_URL}/templates/", headers=headers)
    templates = response.json() if response.ok else []
    return render(
        request,
        'frontend/template-list.html',
        {'templates': templates}
    )


def select_template(request, template_id):
    """Выбор конкретного шаблона."""
    if not request.user.is_authenticated:
        return redirect('login')

    headers = {"Authorization": AUTH_TOKEN}
    response = requests.get(
        f"{settings.API_URL}/templates/{template_id}",
        headers=headers
    )

    if response.ok:
        template = response.json()
        return render(
            request,
            'frontend/detail-template.html',
            {'template': template}
        )
    else:
        return render(
            request,
            'frontend/error-page.html',
            {'error': 'Ошибка загрузки шаблона.'}
        )


def generate_image(request):
    """Генерация изображений."""
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        custom_prompt = request.POST.get('custom_prompt', '').strip()
        selected_template = request.POST.get('template_id', '')

        data = {
            'app_id': 25,
            'user_id': request.user.id,
            'template_id': int(selected_template) if selected_template else None,
        }

        if custom_prompt:
            data['prompt'] = custom_prompt

        response = (
            requests.post(
                settings.API_URL + "/generate-image/",
                headers={"Authorization": AUTH_TOKEN},
                data=data,
                files=request.FILES
            )
            if 'template_file' in request.FILES
            else requests.post(
                settings.API_URL + "/generate-image/",
                json=data,
                headers={"Authorization": AUTH_TOKEN}
            )
        )

        if response.ok:
            result = response.json()
            return render(
                request,
                'frontend/generate-image.html',
                {'image_url': result['image_url'],
                 'result': True}
            )
        else:
            error_message = f'Ошибка ({response.status_code})'
            return render(
                request,
                'frontend/generate-image.html',
                {'error': error_message}
            )

    return render(request, 'frontend/generate-image.html', {})
