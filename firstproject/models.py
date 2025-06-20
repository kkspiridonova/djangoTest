from django.db import models

MAX_LENGHT = 255

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGHT, verbose_name='Наименование категории')
    description = models.TextField(null=True,blank=True,verbose_name='Описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGHT, verbose_name='Наименование коллекции')
    description = models.TextField(null=True,blank=True,verbose_name='Описание')

    def __str__(self):
            return self.name
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

class Clothrs(models.Model):
    name = models.CharField(max_length=MAX_LENGHT, verbose_name='Наименование позиции')
    description = models.TextField(null=True,blank=True,verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.PositiveIntegerField(default=36, verbose_name='Размер')
    colour = models.CharField(max_length=MAX_LENGHT, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True,blank=True,verbose_name='Картинка')
    create_data = models.DateTimeField(auto_now_add=True,verbose_name='Дата добавления на сайт')
    is_exist = models.BooleanField(default=True,verbose_name='Доступность к заказу')

    category = models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name='Категория')
    collection=models.ManyToManyField(Collection, verbose_name='Коллекция')

    def __str__(self):
            return f"{self.name} - ({self.price} рублей.)"
    
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'

class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    TYPE_DELIVERY = [
        (SHOP, 'Вывоз из магазина'),
        (COURIER,'Курьер'),
        (PICKUPPOINT,'Пункт выдачи заказов')
    ]
     
    buyer_firstname = models.CharField(max_length=MAX_LENGHT, default='Unknown',verbose_name="Фамилия")
    buyer_name = models.CharField(max_length=MAX_LENGHT,default='Unknown', verbose_name="Имя")
    buyer_surname = models.CharField(max_length=MAX_LENGHT,blank=True,null=True, verbose_name="Отчетство")
    comment = models.CharField(max_length=MAX_LENGHT,blank=True,null=True, verbose_name="Комментарий")
    delivery_address = models.CharField(max_length=MAX_LENGHT, default='Unknown', verbose_name="Адрес")
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name="Способ доставки")
    date_create=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_finish=models.DateTimeField(blank=True,null=True, verbose_name="Дата завершения")
    clothes = models.ManyToManyField('Clothrs', through='Pos_order',verbose_name="Товар")

    def __str__(self):
            return f"#{self.pk} ({self.buyer_firstname} {self.buyer_name})"
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Pos_order(models.Model):
    clothes = models.ForeignKey("Clothrs", verbose_name="Продукт", on_delete=models.PROTECT)
    order = models.ForeignKey("Order", verbose_name="Заказ", on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=1,verbose_name='Количество продукта')
    discount = models.PositiveIntegerField(default=0,verbose_name='Скидка')

    def __str__(self):
            return f"#{self.order.pk} ({self.order.buyer_firstname} {self.order.buyer_name})"
    
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'


     