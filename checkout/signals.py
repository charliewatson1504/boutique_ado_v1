from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
        created (_type_): _description_
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete

    Args:
        sender (_type_): _description_
        instance (_type_): _description_
    """
    instance.order.update_total()