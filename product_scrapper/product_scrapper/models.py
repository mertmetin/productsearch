
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance.

    """
    return create_engine(URL(**settings.DATABASE))

def create_product_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)
    
class Category(DeclarativeBase):
    __tablename__ = "products_category"
    
    id = Column(Integer, primary_key =True)
    title = Column('title', String)

class SubCategory(DeclarativeBase):
    __tablename__ = "products_subcategory"
    
    id = Column(Integer, primary_key =True)
    title = Column('title', String)
    subcategory = Column('subcategory', Integer, ForeignKey('products_category.id'), nullable = True )

class Products(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "products_product"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    description = Column('description', String)
    url = Column('url', String, nullable=True)
    img = Column('img', String, nullable=True)
    price = Column('price', String, nullable=True)
    online = Column('online', String, nullable=True)
    store = Column('store', String, nullable=True)
    category = Column('category', Integer, ForeignKey('products_category.id'), nullable = True )
    subcategory = Column('subcategory', Integer, ForeignKey('products_subcategory.id'), nullable = True )
