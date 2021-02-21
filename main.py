import artworkDB
from menu import Menu
import view


def main():
    setup()
    menu = make_menu()
    while True:
        choice = view.show_menu_get_choice(menu)
        function = menu.get_function(choice)
        function()
        if choice == 'Q':
            break


        
def setup():
    artworkDB.create_database()


def make_menu():
    menu = Menu()
    menu.add_menu_option('1', 'Add new artist.', add_artist)
    menu.add_menu_option('2', 'Search by artist.', search_by_artist)
    menu.add_menu_option('3', 'Search available art by artist.', search_available_by_artist)
    menu.add_menu_option('4', 'Add artwork.', add_artwork)
    menu.add_menu_option('5', 'Delete artwork.', delete_artwork)
    menu.add_menu_option('6', 'Change artwork availability.', change_availability)
    menu.add_menu_option('Q', 'Quit program.', quite_program)
    return menu


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


def quite_program():
    print('GOODBYE.')

if __name__ == "__main__":
    main()
