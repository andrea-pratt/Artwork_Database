from peewee import SqliteDatabase

db = SqliteDatabase('Artwork.sqlite', pragmas={'foreign_keys': 1})