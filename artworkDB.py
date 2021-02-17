from peewee import *
from config import db
import os


class BaseModel(Model):
    class Meta:
        database = db

class Artist(BaseModel):
    name = CharField(null=False, constraints=[Check('length(name) >= 1'), Check('length(name) <= 30')])
    email = CharField(null=False, unique=True, constraints=[Check('length(email) >=1'), Check('length(email) <= 40')])


    def __str__(self):
        return(f'Name: {self.name}, Email: {self.email}')


class Artwork(BaseModel):
    artist = ForeignKeyField(Artist, backref='name')
    name = CharField(null=False, constraints=[Check('length(name) >=1'), Check('length(name) <= 30')])
    price = DecimalField(null=False, constraints=[Check('price > 0'), Check('length(price) <= 5000')])
    available = BooleanField(null=False)


    def __str__(self):
        return(f'Artist: {self.artist}, Name of Artwork: {self.name}, Price: {self.price}, Available: {self.available}')



def create_database():
    db.connect()
    db.create_tables([Artist, Artwork])



# def search_by_artist():


# def search_available_by_artist():


# def add_artwork():


# def delete_artwork():


# def change_availability():


def add_artist(name, email):
    new_artist = Artist(name=name, email=email)
    new_artist.save()
 
        
def search_by_artist_name(name):
    artist = Artist.get_or_none(Artist.name == name)
    return artist


def update_catches(name, new_catches):
    Juggler.update(catches=new_catches).where(Juggler.name == name).execute()


def delete_by_name(name_to_delete):
    Juggler.delete().where(Juggler.name == name_to_delete).execute()













