class Menu():

    def __init__(self):
        self.menu_options = {}
        self.functions = {}


    def add_menu_option(self, key, text, function):
        self.menu_options[key] = text
        self.functions[key] = function


    def is_valid_choice(self, choice):
        return choice in self.menu_options


    def get_function(self, choice):
        return self.functions[choice]


    def __str__(self):
        menu_options = [f'{key}: {self.menu_options[key]}' for key in self.menu_options.keys()]
        return '\n'.join(menu_options)