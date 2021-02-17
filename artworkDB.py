from peewee import *

db = SqliteDatabase('Artwork.sqlite')

class BaseModel(Model):
    class Meta:
        database = db

class Artist(BaseModel):
    name = CharField(null=False, unique=True, constraints=[Check('length(name) >= 1'), Check('length(name) <= 30')])
    email = CharField(null=False, constraints=[Check('length(email) >=1'), Check('length(email) <= 40')])


    def __str__(self):
        return(f'Name: {self.name}, Email: {self.email}')


class Artwork(BaseModel):
    artist = ForeignKeyField(Artist, backref='name')
    name = CharField(null=False, constraints=[Check('length(name) >=1'), Check('length(name) <= 30')])
    price = DecimalField(null=False, constraints=[Check('price > 0'), Check('length(price) <= 5000')])
    available = BooleanField(null=False)


    def __str__(self):
        return(f'Artist: {self.artist}, Name of Artwork: {self.name}, Price: {self.price}, Available: {self.available}')




