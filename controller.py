import artworkDB
import view

def add_artist():
    artist_name = view.get_user_input('What\'s the name of the new artist?')
    artist_email = view.get_user_input('What\'s the artist\'s email address?')
    artworkDB.add_artist(artist_name, artist_email)


def search_by_artist():
    artist_name = view.get_user_input('What\'s the name of the artist you want to search for?')
    artworks = artworkDB.search_artwork_by_artist(artist_name)
    view.show_artwork_info(artworks)


def search_available_by_artist():
    artist_name = view.get_user_input('What\'s the name of the artist you want to search for?')
    artworks = artworkDB.search_available_by_artist(artist_name)
    view.show_artwork_info(artworks)


def add_artwork():
    artist = view.get_user_input('What\'s the new artist\'s name?')
    artwork_name = view.get_user_input('What is the new artwork called?')
    price = view.get_user_input('What is the price of the artwork?')
    availability = view.get_user_input('Is this item available? (Y/N)')
    artworkDB.add_artwork(artist, artwork_name, price, availability)


def delete_artwork():
    artwork_name = view.get_user_input('What\'s the name of the artwork you want to delete?')
    artworkDB.delete_artwork(artwork_name)


def change_availability():
    artwork_name = view.get_user_input('What artwork would you like to change the availability for?')
    availability = view.get_user_input('Is this available? (Y/N)')
    artworkDB.change_availability(artwork_name, availability)


def display_all_artwork():
    artwork = artworkDB.get_all_artwork()
    view.show_artwork_info(artwork)


def quite_program():
    print('GOODBYE.')
