from django.core.mail import send_mail

from boat.models import Boat
from config import settings
from order.models import Order


def send_order_email(order_item: Order):
    send_mail(
        f'Заявка на покупку лодки: {order_item.name} оставил заявку',
        f'{order_item.name} ({order_item.email}) оставил заявку на покупку лодки {order_item.boat.name}. Сообщение: {order_item.message}',
        settings.EMAIL_HOST_USER,
        [order_item.boat.owner.email]
    )
