
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
    for art in artworks:
        print(f'Artist: {art.artist} Name: {art.name} Price: {art.price}')
