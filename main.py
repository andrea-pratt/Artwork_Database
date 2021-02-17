import artworkDB

def main():
    setup()



def setup():
    artworkDB.create_database()


def make_menu():
    menu = Menu()
    menu.add_menu_option('1', 'Add new artist.', )
    menu.add_menu_option('2', 'Search by artist.', )
    menu.add_menu_option('3', 'Search available art by artist.', )
    menu.add_menu_option('4', 'Add artwork.', )
    menu.add_menu_option('5', 'Delete artwork.', )
    menu.add_menu_option('6', 'Change artwork availability.', )
    menu.add_menu_option('Q', 'Quit program.', )
    return menu

# def add_artist():


# def search_by_artist():


# def search_available_by_artist():


# def add_artwork():


# def delete_artwork():


# def change_availability():



if __name__ == "__main__":
    main()




