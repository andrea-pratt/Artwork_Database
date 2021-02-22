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


    def setup(self):
        # Remove existing data from test database
        self.db = SqliteDatabase(db_path)
        self.db.drop_tables([Artist, Artwork])
        self.db.create_tables([Artist, Artwork])



