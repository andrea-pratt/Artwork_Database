from peewee import Model, CharField, ForeignKeyField, DecimalField, BooleanField, Database, Check, IntegrityError, SqliteDatabase
from config import db_path
import os

# This database will enforce Foreign Key constraints
db = SqliteDatabase(db_path, pragmas={'foreign_keys': 1})

# The base model is used to link all subsequent models to the database
class BaseModel(Model):
    class Meta:
        database = db


"""Artist and Artwork classes are subclasses of the above BaseModel class, and are linked to the database through it"""

class Artist(BaseModel):
    name = CharField(null=False, unique=True, constraints=[Check('length(name) >= 1'), Check('length(name) <= 30')])
    email = CharField(null=False, unique=True, constraints=[Check('length(email) >=1'), Check('length(email) <= 40')])


    def __str__(self):
        return(f'Name: {self.name}, Email: {self.email}')


class Artwork(BaseModel):
    artist = ForeignKeyField(Artist, backref='artworks')
    name = CharField(null=False, unique=True, constraints=[Check('length(name) >=1'), Check('length(name) <= 30')])
    price = DecimalField(null=False, constraints=[Check('price > 0'), Check('length(price) <= 5000')])
    available = BooleanField(null=False)


    def __str__(self):
        return(f'Artist: {self.artist}, Name of Artwork: {self.name}, Price: {self.price}, Available: {self.available}')
