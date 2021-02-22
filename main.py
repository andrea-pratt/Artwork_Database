import setup
import view

"""Highest level functionality of the application - deligates most high level functions to controller.py"""
def main():
    setup.setup_database()
    menu = setup.make_menu()
    while True:
        choice = view.show_menu_get_choice(menu)
        function = menu.get_function(choice)
        function()
        if choice == 'Q':
            break

       
if __name__ == "__main__":
    main()
