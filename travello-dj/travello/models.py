from typing import Text
from django.db import models
# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

class Destination(models.Model):
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"))
    price = models.IntegerField(_("price"))
    image = models.ImageField(_("image"), upload_to="destinations")
    offer = models.BooleanField(_("special offer") , default=False)
    slug = models.SlugField(_("slug") , blank=True , null=True)

    
    class Meta:
        verbose_name = _("Destination")
        verbose_name_plural = _("Destinations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Destination_detail", kwargs={"pk": self.pk})
    
    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Destination , self).save(*args, **kwargs)




class Contact(models.Model):
    name = models.CharField(_("name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254)
    subject = models.TextField(_("subject"))

    

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})
