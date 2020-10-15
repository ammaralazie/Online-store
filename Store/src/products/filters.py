import django_filters
from . models import Product

class ProductsFilter(django_filters.FilterSet) :
    class Meta:
        model =Product
        fields='__all__'
        exclude=['PRDBrand','PRDSlug','PRDImage','PRDCreated','PRDPrice','PRDDiscount','PRDNew','PRDBeastsaller','PRDCost']
