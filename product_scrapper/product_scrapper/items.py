from scrapy.contrib.djangoitem import DjangoItem
from products.models import Product, Category, SubCategory

class ProductItem(DjangoItem):
    django_model = Product
    
class CategoryItem(DjangoItem):
    django_model = Category
    
class SubCategoryItem(DjangoItem):
    django_model = SubCategory
