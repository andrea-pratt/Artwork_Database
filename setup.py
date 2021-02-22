from artworkDB import create_database
from menu import Menu
import controller

def setup_database():
    create_database()


def make_menu():
    menu = Menu()
    menu.add_menu_option('1', 'Add new artist.', controller.add_artist)
    menu.add_menu_option('2', 'Search by artist.', controller.search_by_artist)
    menu.add_menu_option('3', 'Search available art by artist.', controller.search_available_by_artist)
    menu.add_menu_option('4', 'Add artwork.', controller.add_artwork)
    menu.add_menu_option('5', 'Delete artwork.', controller.delete_artwork)
    menu.add_menu_option('6', 'Change artwork availability.', controller.change_availability)
    menu.add_menu_option('7', 'Display all artwork', controller.display_all_artwork)
    menu.add_menu_option('Q', 'Quit program.', controller.quite_program)
    return menu