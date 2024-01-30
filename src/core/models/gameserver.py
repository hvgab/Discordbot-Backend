from django import models
from django.urls import reverse


class GameServer(models.Model):

    url = models.URLField(_("url"), max_length=200)
    port = models.IntegerField(_("port"))

    class Meta:
        verbose_name = _("gameserver")
        verbose_name_plural = _("gameservers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gameserver_detail", kwargs={"pk": self.pk})
