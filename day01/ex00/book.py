from recipe import Recipe
import datetime

class Book:
    def __init__(self):
        self.name = 'Grandma\'s book'
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {'starter' : [], 'lunch' : [], 'dessert' : []}

    def get_recipe_by_name(self, name):
        if not name:
            print("No recipe, grandma can't guess\n")
        exist = 0
        for rtype in self.recipes_list:
            for recipe in self.recipes_list[rtype]:
                if recipe.name == name:
                    print(str(recipe), '\n')

    def get_recipes_by_types(self, recipe_type):
        if not recipe_type:
            print("No type, grandma can't guess\n")
            return
        if recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                print(str(recipe), '\n')
        else:
            print('No type with this name\n')
    
    def add_recipe(self, recipe):
        if not recipe:
            print("No recipe, grandma can't guess\n")
            return
        if not isinstance(recipe, Recipe):
            raise TypeError('Only Recipe are allowed for recipe')
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()
