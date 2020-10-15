from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    slug=models.SlugField(null=True,blank=True)
    image=models.ImageField(upload_to='image_profile/',blank=True,null=True,verbose_name=_("Profile_Image"))
    country = CountryField(verbose_name=_("user_country"),default='Iraq')
    address=models.CharField(max_length=100)
    join_date=models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return '%s' %(self.user)

    def save(self,*args,**kwargs):
        if not self.slug :
            self.slug=slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)



    def get_abslute_url(self):
        return reverse('accounts:prfile_detail',kwargs('slug',self.slug))
    class Meta :
        verbose_name=_("Profile")
        verbose_name_plural=_("Profile")
def create_profile(sender,**kwargs):
    if kwargs['created'] :
        obj_profile=Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)

# Create your models here.
