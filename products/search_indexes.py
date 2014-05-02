import datetime
from django.utils import timezone
from haystack import indexes
from haystack.query import SearchQuerySet
from models import *



class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text=indexes.CharField(document=True, use_template=True)
    price = indexes.CharField(model_attr='price')
    
    
    #Filters
    category = indexes.CharField(model_attr='category', faceted=True)
    subcategory = indexes.CharField(model_attr='subcategory', faceted=True)
    
    def get_model(self):
        return Product
   
