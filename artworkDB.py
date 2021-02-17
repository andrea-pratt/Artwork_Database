from peewee import *

db = SqliteDatabase('Artwork.sqlite')

class Artist(Model):
    name = CharField(null=False, unique=True, constraints=[Check('length(name) >= 1'), Check('length(name) <= 30')])
    email = CharField(null=False, constraints=[Check('length(email) >=1'), Check('length(email) <= 40')])

    class Meta:
        database = db


    def __str__(self):
        return(f'Name: {self.name}, Email: {self.email}')


class Artwork(Model):
    artist = CharField(null=False, constraints=[Check('length(artist) >= 1'), Check('length(artist) <= 30')])
    name = CharField(null=False, constraints=[Check('length(name) >=1'), Check('length(name) <= 30')])
    price = DecimalField(null=False, constraints=[Check('price > 0'), Check('length(price) <= 5000')])
    available = BooleanField(null=False)

    class Meta:
        database = db


    def __str__(self):
        return(f'Artist: {self.artist}, Name of Artwork: {self.name}, Price: {self.price}, Available: {self.available}')


db.connect()
db.create_tables([Artist, Artwork])