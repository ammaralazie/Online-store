from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Product (models.Model):
    PRDName=models.CharField(max_length=100,verbose_name=_("product Name"))
    PRDCategory=models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name=_("Product Category"),null=True,blank=True)
    PRDBrand=models.ForeignKey('settings.Brand',on_delete=models.CASCADE,verbose_name=_("Brand Product"),null=True,blank=True)
    PRDSlug=models.SlugField(null=True,blank=True)
    PRDDescribtion=models.TextField(verbose_name=_("product decribtion"))
    PRDImage=models.ImageField(upload_to="media/",verbose_name=_("Iamge"),null=True,blank=True)
    PRDCreated=models.DateTimeField(verbose_name=_("created at"))
    PRDPrice=models.DecimalField(default=0,max_digits=5,decimal_places=2,verbose_name=_("Price"))
    PRDDiscount=models.DecimalField(default=0,max_digits=5,decimal_places=2,verbose_name=_("Discount"))
    PRDNew=models.BooleanField(default=True)
    PRDDigital=models.BooleanField(default=False)
    PRDCost=models.DecimalField(default=0,max_digits=5,decimal_places=2,verbose_name=_(" cost"))


    def save(self,*args,**kwargs):
        if not self.PRDSlug:
            self.PRDSlug=slugify(self.PRDName)
        super(Product,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('product:product_detail',kwargs={'slug':self.PRDSlug})

    def __str__(self):
        return self.PRDName
    class Meta :
        verbose_name=_("Product")
        verbose_name_plural=_("Products")

class ProductImage(models.Model):
    PRDIProdect=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("Product"))
    PRDIImage=models.ImageField(upload_to="media/",verbose_name=_("Iamge"),null=True,blank=True)
    def __str__(self):
        return str(self.PRDIProdect)
    class Meta :
        verbose_name=_("ProductImage")
        verbose_name_plural=_("ProductImages")
class Category(models.Model):
    CATName=models.CharField(max_length=50,verbose_name="Name")
    CATParent=models.ForeignKey('self',on_delete=models.CASCADE,limit_choices_to={'CATParent__isnull':True},null=True,blank=True,verbose_name="Parent Namae")
    CATDescription=models.TextField(verbose_name="Category Description")
    CATImg=models.ImageField(upload_to='media/',verbose_name="Category Image")
    def __str__(self):
        return self.CATName
    class Meta :
        verbose_name=_("Category")
        verbose_name_plural=_("Categories")
class Product_Alternntive(models.Model):
    PALNPoduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='main_product',verbose_name=_("Nmae"))
    PALNAlternative=models.ManyToManyField(Product,related_name='product_alernative', verbose_name=_("Alterntives"))

    def __str__(self):
        return str(self.PALNPoduct)
    class Meta:
        verbose_name=_("Product_Alternntive")
        verbose_name_plural=_("Products_Alternntive")
class Product_Aessories(models.Model):
    PACCPoduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='mainAccessories_product',verbose_name=_("Name"))
    PACCAlternative=models.ManyToManyField(Product,related_name='product_Accessories',verbose_name=_("Accessories"))

    def __str__(self):
        return str(self.PACCPoduct)
    class Meta:
        verbose_name=_("Product_Aessory")
        verbose_name_plural=_("Product_Aessories")
class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complate=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=100,null=True)
    def __str__(self) :
        return str(self.id)

    @property
    def shipping(self):
        shipping=False
        orderitem=self.orderitems_set.all()
        for i in orderitem :
            if i.producte.PRDDigital == False :
                shipping=True
        return shipping        
    @property
    def get_total_price(self):
        orderitem=self.orderitems_set.all()
        total_price=sum([item.get_total for item in orderitem])
        return total_price

    @property
    def get_total_items(self):
        orderitem=self.orderitems_set.all()
        total_items=sum([item.quantity for item in orderitem])
        return total_items

class OrderItems(models.Model):
    producte=models.ForeignKey(Product,on_delete=models.CASCADE ,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE ,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_add=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.producte.PRDPrice *self.quantity
        return total
class ShippingAderess(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE ,null=True)
    address=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address
