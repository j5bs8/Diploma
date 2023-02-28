from django.db import models

# Create your models here.
class Product(models.Model):
    model = models.CharField('Модель', max_length=100, default='')
    form_factor = models.ForeignKey('Factor', on_delete=models.SET_NULL, null=True)
    cpu = models.ForeignKey('Cpu', on_delete=models.SET_NULL, null=True)
    memory = models.ForeignKey('Memory', on_delete=models.SET_NULL, null=True)
    pci = models.ForeignKey('Pci', on_delete=models.SET_NULL, null=True)
    back_panel = models.ForeignKey('BackPannel', on_delete=models.SET_NULL, null=True)
    audio = models.ForeignKey('Audio', on_delete=models.SET_NULL, null=True)
    network = models.ForeignKey('Network', on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey('Schema', on_delete=models.SET_NULL, null=True)
    shop_url = models.TextField('Ссылка на покупку', default='url')

    def __str__(self):
        return self.model
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Schema(models.Model):
    title = models.CharField('Название схемы', max_length=40)
    image = models.ImageField('Схема', upload_to='static/catalog/media')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Схема'
        verbose_name_plural = 'Схемы'


class Factor(models.Model):
    name = models.CharField('Наименование', max_length=10)
    height = models.FloatField('Высота')
    weight = models.FloatField('Ширина')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Форм фактор'
        verbose_name_plural = 'Форм факторы'


class Cpu(models.Model):
    name = models.CharField('Наименование', max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сокет'
        verbose_name_plural = 'Сокеты'


class Memory(models.Model):
    memory_type = models.ForeignKey('Memory_Types', on_delete=models.SET_NULL, null=True)
    max_size = models.ForeignKey('Memory_Max_Sizes', on_delete=models.SET_NULL, null=True)
    memory_slot = models.ForeignKey('Memory_Slots', on_delete=models.SET_NULL, null=True)
    memory_freq = models.ForeignKey('Memory_Freq', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        res_str = str(self.memory_type) + ' ' + str(self.max_size) + 'GB ' + str(self.memory_slot) + ' слота ' + str(self.memory_freq) + ' Мгц'
        return res_str

    class Meta:
        verbose_name = 'Память'
        verbose_name_plural = 'Память'

class Memory_Types(models.Model):
    type = models.CharField('Тип', max_length=10)

    def __str__(self):
        return self.type
    
    class Meta:
        verbose_name = 'Тип памяти'
        verbose_name_plural = 'Типы памяти'

class Memory_Max_Sizes(models.Model):
    max_size = models.SmallIntegerField('Объем')
    
    def __str__(self):
        return str(self.max_size)
    class Meta:
        verbose_name = 'Макс. объем'
        verbose_name_plural = 'Макс. объемы'

class Memory_Slots(models.Model):
    slot = models.SmallIntegerField('Кол-во')

    def __str__(self):
        return str(self.slot)
    
    class Meta:
        verbose_name = 'Кол-во слотов'
        verbose_name_plural = 'Кол-во слотов'

class Memory_Freq(models.Model):
    freq = models.SmallIntegerField('Частота')

    def __str__(self):
        return str(self.freq)
    
    class Meta:
        verbose_name = 'Частота памяти'
        verbose_name_plural = 'Частоты памяти'


class Pci(models.Model):
    name = models.CharField('Название', max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тип PCI'
        verbose_name_plural = 'Типы PCI'

class BackPannel(models.Model):
    information = models.TextField('Информация')

    def __str__(self):
        return self.information
    
    class Meta:
        verbose_name = 'Задняя панель'
        verbose_name_plural = 'Задние панели'

class Audio(models.Model):
    audio_chipset = models.CharField('Чипсет', max_length=50)

    def __str__(self):
        return self.audio_chipset
    
    class Meta:
        verbose_name = 'Аудио чипсет'
        verbose_name_plural = 'Аудио чипсеты'

class Network(models.Model):
    adapter = models.CharField('Адаптер', max_length=50)
    speed = models.SmallIntegerField('Срокость адаптера')

    def __str__(self):
        return self.adapter
    
    class Meta:
        verbose_name = 'Сетевой адаптер'
        verbose_name_plural = 'Сетевые адаптеры'