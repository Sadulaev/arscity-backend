from django.db import models


class WorkExample(models.Model):
    title = models.CharField('Заголовок',max_length=255)
    address = models.CharField('Адрес', max_length=255)
    description = models.TextField('Описание')
    image1 = models.ImageField('Изображение 1', upload_to='work_examples/', blank=True, null=True)
    image2 = models.ImageField('Изображение 2', upload_to='work_examples/', blank=True, null=True)
    image3 = models.ImageField('Изображение 3', upload_to='work_examples/', blank=True, null=True)
    image4 = models.ImageField('Изображение 4', upload_to='work_examples/', blank=True, null=True)


    class Meta:
        verbose_name="Приемры работ"
        verbose_name_plural="Приемры работ"
    def __str__(self):
        return self.title