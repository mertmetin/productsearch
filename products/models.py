from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    
    def __unicode__(self):
       return u'%s' % (self.title)
       
class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(Category, db_column='parent')
    
    def __unicode__(self):
       return u'%s' % (self.title)



class Product(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    price = models.CharField(max_length=16)
    online = models.CharField(max_length=5, null=True)
    store = models.CharField(max_length=5, null=True)
    category = models.ForeignKey(Category, db_column='category')
    subcategory = models.ForeignKey(SubCategory, db_column='subcategory')
    
    def title_as_list(self):
        return self.title.split(' ')


