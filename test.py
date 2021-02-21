import unittest 
from unittest import TestCase
from unittest.mock import patch
from peewee import *

import config
db = 'test_artwork.sqlite'
db_config.database_path = db_path 

from models import Tree
import controller 
import database
from database import TreeError

class TreeControllerTest(TestCase):


    def setUp(self):
        # connect to test database, drop and create tables 
        self.db = SqliteDatabase(db_path)
        self.db.drop_tables([Tree])
        self.db.create_tables([Tree])


    @patch('ui.get_string', return_value='oak')
    @patch('ui.get_positive_float', return_value=50)
    def test_add_tree(self, mock_get_float, mock_get_string):
        controller.add_tree()
        oak_tree = Tree.get_or_none(Tree.name=='oak' and Tree.max_height==50)
        self.assertIsNotNone(oak_tree)


    @patch('ui.get_string', return_value='oak')
    @patch('ui.get_positive_float', return_value=50)
    def test_add_tree_duplicate(self, mock_get_float, mock_get_string):
        Tree(name='oak', max_height=40).save()
        controller.add_tree()
        tree_count = Tree.select().count()
        self.assertEqual(1, tree_count)  # only one Tree



class TreeDatabaseTest(TestCase):

    def setUp(self):
        # connect to test database, drop and create tables 
        self.db = SqliteDatabase(db_path)
        self.db.drop_tables([Tree])
        self.db.create_tables([Tree])


    def test_add_tree(self):
        database.add_tree('oak', 50)
        oak_tree = Tree.get_or_none(Tree.name=='oak' and Tree.max_height==50)
        self.assertIsNotNone(oak_tree)


    def test_add_tree_duplicate(self):
        Tree(name='oak', max_height=40).save()
        with self.assertRaises(TreeError):
            database.add_tree('oak', 50)
        
