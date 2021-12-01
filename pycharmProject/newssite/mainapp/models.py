from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone


class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    full_text = models.TextField('Статья')
    author = models.CharField('Автор', max_length=50)
    tag = TaggableManager()
    date = models.DateTimeField('Дата', default=timezone.now)
    image = models.ImageField('Добавить изображение', upload_to='images', blank=True)

    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.title
