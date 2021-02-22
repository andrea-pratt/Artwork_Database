import unittest 
from unittest import TestCase
from unittest.mock import patch
from peewee import Model, CharField, ForeignKeyField, DecimalField, BooleanField, Database, Check, IntegrityError, SqliteDatabase

import config
db_path = 'test_artwork.db'
config.db_path = db_path

from models import Artist, Artwork
import artworkDB

class TestArtworkDB(TestCase):


    def setUp(self):
        # Remove existing data from test database and recreate tables
        self.db = SqliteDatabase(db_path)
        self.db.drop_tables([Artist, Artwork])
        self.db.create_tables([Artist, Artwork])


    def add_generic_sample_data(self):  # Adds sample data for my test methods to work with if needed
        artworkDB.add_artist('Bob', 'bob@gmail.com')
        artworkDB.add_artist('Maria', 'maria@gmail.com')

        artworkDB.add_artwork('Bob', 'Simplicity Defined', 3400.00, True)
        artworkDB.add_artwork('Bob', 'Life Without Entropy', 8200.00, True)
        artworkDB.add_artwork('Bob', 'Love in the Winter', 2200.00, False)

        artworkDB.add_artwork('Maria', 'Waves Abound', 6700.00, False)
        artworkDB.add_artwork('Maria', 'A Distant Mountain', 960.00, False)
        artworkDB.add_artwork('Maria', 'In the End', 7600.00, True)


    def test_add_artist(self):  # Tests to see if it can retrieve an artists data after adding it to the database
        self.add_generic_sample_data()
        artworkDB.add_artist('Matthew', 'matthew@gmail.com')

        artist = Artist.get_or_none(Artist.name=='Matthew', Artist.email=='matthew@gmail.com')
        self.assertIsNotNone(artist)


    def test_add_artist_name_already_exists(self):  # Makes sure an artist can't be added twice to the database
        self.add_generic_sample_data()
        with self.assertRaises(IntegrityError):
            artworkDB.add_artist('Bob', 'bobbyman@gmail.com')


    def test_add_artist_email_already_exists(self):  # Makes sure an artist's email can't be added twice
        self.add_generic_sample_data()
        with self.assertRaises(IntegrityError):
            artworkDB.add_artist('Bobby', 'bob@gmail.com')


    def test_add_artist_name_null(self):  # Make sure database won't accept a null artist name 
        with self.assertRaises(IntegrityError):
            artworkDB.add_artist(None, 'random_email@gmail.com')


    def test_add_artist_email_null(self):  # Makes sure database won't accept a null artist email
        with self.assertRaises(IntegrityError):
            artworkDB.add_artist('Harry', None)


    def test_add_artwork(self):  # Try to retrieve data about an artwork after adding it to the database
        artworkDB.add_artist('Bob', 'bob@comcast.net')
        artworkDB.add_artwork('Bob', 'Air is Empathy', 6600, True)
        artwork = Artwork.get_or_none(Artwork.name == 'Air is Empathy', Artwork.price == 6600, Artwork.available == True)
        self.assertIsNotNone(artwork)


    def test_delete_artwork_by_name(self):  # Makes sure artwork is gone after calling the method to delete it
        self.add_generic_sample_data()
        artworkDB.delete_artwork('Simplicity Defined')
        artwork = Artwork.get_or_none(Artwork.name == 'Simplicity Defined')
        self.assertIsNone(artwork)


    def test_change_artwork_availability(self): # Make sure availability status of artwork is changed correctly
        self.add_generic_sample_data()
        artworkDB.change_availability('Simplicity Defined', False)
        artwork = Artwork.get_or_none(Artwork.name == 'Simplicity Defined', Artwork.available == False)
        self.assertIsNotNone(artwork)


    def test_search_artwork_by_artist(self):  # Try pulling up all artwork for a given artist
        artworkDB.add_artist('Bob', 'bob@gmail.com')
        artworkDB.add_artwork('Bob', 'Life of Insanity', 90, False)
        artwork = artworkDB.search_artwork_by_artist('Bob')
        for art in artwork:
            self.assertEqual(art.name, 'Life of Insanity')

 
    def test_search_available_by_artist(self):  # Makes sure only available artwork is returned for this function
        artworkDB.add_artist('Bob', 'bob@gmail.com')
        artworkDB.add_artwork('Bob', 'Life of Insanity', 90, True)
        artworkDB.add_artwork('Bob', 'Modern Age', 400, False)
        artworkDB.add_artwork('Bob', 'Rain and Snow', 448, False)
        artwork = artworkDB.search_available_by_artist('Bob')
        for art in artwork:
            self.assertEqual(art.name, 'Life of Insanity')

        

if __name__ == '__main__':
    unittest.main()
