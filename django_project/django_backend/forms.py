from django.forms import ModelForm
from .models import FileUploader


class FileUploaderForm(ModelForm):
    class Meta:
        model = FileUploader
        fields = ['file']
