from django.conf import settings
from firstproject.models import Clothrs

class Basket:
    """Класс для управления корзиной товаров в сессии"""

    def __init__(self, request):
        """Инициализация корзины"""
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        """Итерация по товарам в корзине"""
        product_ids = self.basket.keys()
        product_list = Clothrs.objects.filter(pk__in=product_ids)

        basket = self.basket.copy()
        for product in product_list:
            basket[str(product.pk)]['product'] = product

        for item in basket.values():
            item['total_price'] = float(item['price']) * int(item['count'])
            yield item

    def __len__(self):
        """Общее количество товаров в корзине"""
        return sum(int(item['count']) for item in self.basket.values())

    def save(self):
        """Сохранение корзины в сессии"""
        self.session[settings.BASKET_SESSION_ID] = self.basket
        self.session.modified = True

    def add(self, product, count=1, update_count=False):
        """
        Добавление товара в корзину или обновление его количества
        :param product: Объект товара
        :param count: Количество для добавления
        :param update_count: Флаг обновления количества (True - установить, False - добавить)
        """
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {
                'count': 0,
                'price': str(product.price)
            }

        if update_count:
            self.basket[product_id]['count'] = count
        else:
            self.basket[product_id]['count'] += count
        self.save()

    def remove(self, product):
        """
        Удаление товара из корзины
        :param product: Объект товара для удаления
        """
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def get_total_price(self):
        """
        Расчет общей стоимости всех товаров в корзине
        :return: Общая стоимость
        """
        return sum(
            float(item['price']) * int(item['count'])
            for item in self.basket.values()
        )

    def clear(self):
        """
        Полная очистка корзины
        """
        if settings.BASKET_SESSION_ID in self.session:
            del self.session[settings.BASKET_SESSION_ID]
            self.session.modified = True
