from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_('Название'), max_length=100)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name = models.CharField(_('Назначение'), max_length=100)
    def __str__(self):
        return self.name

class Feature(models.Model):
    name = models.CharField(_('Особенность'), max_length=100)
    def __str__(self):
        return self.name

class Tile(models.Model):
    name = models.CharField(_('Название'), max_length=200)
    description = models.TextField(_('Описание'))
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    discount = models.DecimalField(_('Скидка'), max_digits=5, decimal_places=2, default=0.0)
    image = models.ImageField(_('Фотография'), upload_to='tiles/')
    category = models.ForeignKey(Category, verbose_name=_('Категория'), on_delete=models.CASCADE)
    material = models.CharField(_('Материал'), max_length=100)
    room = models.CharField(_('Помещение'), max_length=100)
    purpose = models.ManyToManyField(Purpose, verbose_name=_('Назначение'))
    size = models.CharField(_('Размер'), max_length=100)
    color = models.CharField(_('Цвет'), max_length=100)
    pattern = models.CharField(_('Рисунок'), max_length=100)
    surface = models.CharField(_('Поверхность'), max_length=100)
    shape = models.CharField(_('Форма'), max_length=100)
    is_new = models.BooleanField(_('Новинка'), default=False)
    is_promo = models.BooleanField(_('Акция'), default=False)
    style = models.CharField(_('Стиль'), max_length=100)
    features = models.ManyToManyField(Feature, verbose_name=_('Особенности'))
    country = models.CharField(_('Страна'), max_length=100)
    collection = models.CharField(_('Коллекция'), max_length=100)

    def __str__(self):
        return self.name

class Laminate(models.Model):
    name = models.CharField(_('Название'), max_length=200)
    description = models.TextField(_('Описание'))
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    discount = models.DecimalField(_('Скидка'), max_digits=5, decimal_places=2, default=0.0)
    image = models.ImageField(_('Фотография'), upload_to='laminates/')
    category = models.ForeignKey(Category, verbose_name=_('Категория'), on_delete=models.CASCADE)
    country = models.CharField(_('Страна'), max_length=100)
    grade = models.CharField(_('Класс'), max_length=50)
    thickness = models.DecimalField(_('Толщина'), max_digits=4, decimal_places=1)
    water_resistant = models.BooleanField(_('Влагостойкость'), default=False)
    chamfer = models.CharField(_('Фаска'), max_length=100)
    pattern = models.CharField(_('Рисунок'), max_length=100)
    surface = models.CharField(_('Поверхность'), max_length=100)
    wood_type = models.CharField(_('Порода дерева'), max_length=100)
    is_promo = models.BooleanField(_('Акция'), default=False)

    def __str__(self):
        return self.name

