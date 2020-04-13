cookbook = {'sandwich' :  {'ingredients' : ['ham', 'bread', 'cheese', \
'tomatoes'] , 'meal' : 'lunch', 'prep_time' : 10}, \
'cake' : {'ingredients' : ['flour', 'sugar', 'eggs'] , 'meal' : 'dessert', \
'prep_time' : 60}, \
'salad' : {'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'] , \
'meal' : 'lunch', 'prep_time' : 15}}

def print_my_cookbook(cookbook):
    print('Let\'s see what we have here...\n')
    for recipe in cookbook:
        print_recipe(recipe)
        print('\n')
        

def print_recipe(recipe=''):
    if recipe == '':
        print("\nNo recipe, grandma can't guess\n")
        return
    if not recipe in cookbook:
        print("\nGrandma never wrote this recipe\n")
        return
    print('Recipe for grandma\'s {}'.format(recipe))
    for value in cookbook[recipe]:
            if value == 'ingredients':
                print('Ingredients :')
                for ingr in cookbook[recipe][value]:
                    print('  -', ingr)
            if value == 'meal':
                print('For {} time !'.format(cookbook[recipe][value]))
            if value == 'prep_time':
                print('Take only {} minutes !'.format(cookbook[recipe][value]))

def delete_recipe(recipe):
    if recipe == '':
        print("\nNo recipe, grandma can't guess\n")
        return
    if not recipe in cookbook:
        print("\nGrandma never wrote this recipe\n")
        return
    del cookbook[recipe]

def new_recipe(name='', ingr='', meal_t='', time=''):
    if name == '' or ingr == '' or meal_t == '' or time == '':
        print("\nSomething is missing, grandma can't guess\n")
        return
    if name in cookbook:
        print("\nGrandma already wrote it\n")
        return
    cookbook[name] = dict(ingredients = ingr, meal = meal_t, prep_time = time)


print('You have found the old grandma\'s cookbook\n what are you going to do ?\
')

choice = 0
ing_list = []
while choice != 5:
    choice = int(input('1.Add a recipe\n2.Delete a recipe\n3.Print a recipe\
    \n4.Print the cookbook\
    \n5.Leave the book the alone\n\n'))
    if choice == 1:
        print('\nBe careful with the pages my dear...\n\
        They are older than you\n\n')
        print('\nFirst choose a name for the recipe:\n')
        name = input()
        print('\nWrite the ingredient if you\'re done tap enter with nothing')
        ingre = input()
        while ingre != '':
            ing_list.append(ingre)
            ingre = input()
        print('\nWhat kind of meal is it?')
        meal_t = input()
        print('\nHow many time it takes for a mortal to cook it?')
        prep_time = int(input())
        new_recipe(name, ing_list, meal_t, prep_time)
        ingre = ''
        ing_list = []
        name = ''
        meal_t = ''
        prep_time = 0
    if choice == 2:
        print('\nYou can burn one of this page:\n')
        for recipe in cookbook:
            print('{}'.format(recipe))
        print('choose:')
        name = input()
        delete_recipe(name)
        name = ''
    if choice == 3:
        print('\nYou can look at one of this page:\n')
        for recipe in cookbook:
            print('{}'.format(recipe))
        print('choose:')
        name = input()
        print_recipe(name)
        name = ''
    if choice == 4:
        print_my_cookbook(cookbook)
print('The book is closed')
