from django.db.models.signals import post_save, post_delete
from django.dispatch import reciever

from .modles import OrderLineItem


@reciver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Updates order total on the line item update and create feature
    """
    instance.order.update_total()

@reciver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Updates order total on the line item delete feature
    """
    instance.order.update_total()
    