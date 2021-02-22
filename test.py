import unittest 
from unittest import TestCase
from unittest.mock import patch
from peewee import Model, CharField, ForeignKeyField, DecimalField, BooleanField, Database, Check, IntegrityError, SqliteDatabase

import config
db_path = 'test_artwork.sqlite'
config.db_path = db_path

from models import Artist, Artwork
import artworkDB

class TestArtworkDB(TestCase):


    def setUp(self):
        # Remove existing data from test database
        self.db = SqliteDatabase(db_path)
        self.db.drop_tables([Artist, Artwork])
        self.db.create_tables([Artist, Artwork])

    def add_generic_sample_data(self):
        artworkDB.add_artist('Bob', 'bob@gmail.com')
        artworkDB.add_artist('Maria', 'maria@gmail.com')

        artworkDB.add_artwork('Bob', 'Simplicity Defined', 3400.00, True)
        artworkDB.add_artwork('Bob', 'Life Without Entropy', 8200.00, True)
        artworkDB.add_artwork('Bob', 'Love in the Winter', 2200.00, False)

        artworkDB.add_artwork('Maria', 'Waves Abound', 6700.00, False)
        artworkDB.add_artwork('Maria', 'A Distant Mountain', 960.00, False)
        artworkDB.add_artwork('Maria', 'In the End', 7600.00, True)


       



