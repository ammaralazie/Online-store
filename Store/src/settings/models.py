from django.db import models
from django.utils.translation import ugettext_lazy as _


class Brand(models.Model):
    BRDName=models.CharField(max_length=40,verbose_name=_("Nmae"))
    BRBDesc=models.TextField(verbose_name=_("Brand  Description"),null=True,blank=True)
    def __str__(self):
      return str(self.BRDName)

    class Meta:
        verbose_name=_("Brand")
        verbose_name_plural=_("Brands")


class Variant(models.Model):
    VARName=models.CharField(max_length=40,verbose_name=_("Nmae"))
    VARDesc=models.TextField(verbose_name=_("Variant  Description"),null=True,blank=True)
    def __str__(self):
      return str(self.VARName)

    class Meta:
        verbose_name=_("Variant")
        verbose_name_plural=_("VariantS")
