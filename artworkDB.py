from peewee import *
from config import db
import os


class BaseModel(Model):
    class Meta:
        database = db

class Artist(BaseModel):
    # For simplicity, I've made the name a unique value
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



def create_database():
    db.connect()
    db.create_tables([Artist, Artwork])


def search_artwork_by_artist(name):
    artworks = Artwork.select().join(Artist).where(Artist.name == name)
    for art in artworks:
        print(f'Artist: {art.artist} Name: {art.name} Price: {art.price}')


def search_available_by_artist(name):
    artworks = Artwork.select().join(Artist).where((Artist.name == 'Bob') & (Artwork.available == True))
    
    for art in artworks:
        print(f'Artist: {art.artist} Name: {art.name} Price: {art.price}')


def get_artist_id(name):
   artist = Artist.get_or_none(Artist.name == name)
   artist_id = artist.id
   return artist_id


"""If the artist exists, add the artist, else, create the artist"""
def add_artwork(artist, name, price, availability):
    try:
        artist_id = get_artist_id(artist)
        new_artwork = Artwork(artist=artist_id, name=name, price=price, available=availability)
        new_artwork.save()
        return f'The artwork \'{name}\' by {artist} was added successfully'
    except IntegrityError as e:
        # Put some code here that asks for the new artist's information
        print(e)

    
def delete_artwork(artwork_name):
    Artwork.delete().where(Artwork.name == artwork_name).execute()


def change_availability(artwork_name, availability):
    Artwork.update(available=availability).where(Artwork.name == artwork_name).execute()


def add_artist(name, email):
    new_artist = Artist(name=name, email=email)
    new_artist.save()
 
        
def search_by_artist_name(name):
    artist = Artist.get_or_none(Artist.name == name)
    return artist















