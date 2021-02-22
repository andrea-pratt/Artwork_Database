
def show_menu_get_choice(menu):
    while True:
        print(menu)
        choice = input('Enter choice? ').upper()
        if menu.is_valid_choice(choice):
            return choice
        else:
            print('Not a valid choice, try again.')


def get_user_input(prompt):
    return input(prompt)


def user_message(message):
    print(message)


def show_artwork_info(artworks):
    print('\n\n')
    for art in artworks:
        print(f'Artist: {art.artist.name}   Name: {art.name}    Price: {art.price}  Available: {art.available}')
    print('\n\n')