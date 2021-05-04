from django.db import models
from django.utils.translation import gettext as _


from account.models import User


class Flight(models.Model):
    boarding = models.CharField(_("boarding location"), max_length=120)
    destination = models.CharField(_("destination location"), max_length=120)
    flight_datetime = models.DateTimeField(_("flight date-time"))
    STATUS_CHOICES = (
        ('booked', 'booked'),
        ('available', 'available'),
        ('cancelled', 'cancelled'),
    )
    status = models.CharField(
        _("status"), max_length=50, choices=STATUS_CHOICES)
    booked_by = models.ForeignKey(User, verbose_name=_(
        "flight booked by"), on_delete=models.SET_NULL, null=True, blank=True)
