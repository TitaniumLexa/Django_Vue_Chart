from django.db import models
from django.contrib import admin


class FileUploader(models.Model):
    file = models.FileField(upload_to='uploads/', )
    upload_date = models.DateTimeField(auto_now=True, db_index=True)


admin.site.register(FileUploader)
