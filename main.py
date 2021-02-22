import setup
import view


def main():
    setup.setup_data()
    menu = setup.make_menu()
    while True:
        choice = view.show_menu_get_choice(menu)
        function = menu.get_function(choice)
        function()
        if choice == 'Q':
            break

       
if __name__ == "__main__":
    main()
