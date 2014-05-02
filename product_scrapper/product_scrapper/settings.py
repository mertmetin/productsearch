BOT_NAME = 'product_scrapper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['product_scrapper.spiders']

NEWSPIDER_MODULE = 'product_scrapper.spiders'

USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['product_scrapper.pipelines.ProductPipeline']


DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'postgres', 
            'password': 'fenderpass', 
            'database': 'product'}
 

from django.conf import settings
import sys
sys.path.append('/home/mert/Desktop/productsearch')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


