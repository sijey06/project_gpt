from django import forms


class ImageGenerationForm(forms.Form):
    prompt = forms.CharField(label='Описание изображения', required=True)
    template_file = forms.ImageField(label='Шаблон', required=False)
