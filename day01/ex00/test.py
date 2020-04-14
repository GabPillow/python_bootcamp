from book import Book
from recipe import Recipe

#RECIPE PART

print('####### RECIPE PART ######\n')
#Test:01 normal [OK]
print('|   TEST: 01 NORMAL   |\nError : none\n')
test = Recipe('Pot au feu', 5, 145, ['boeuf', 'carrotte', 'vin'], \
'Le plat préféré de ma femme', 'lunch')
print(str(test))
print('CHECK: [OK]\n')

# Test: 02 NOTHING [OK]
try:
    print('|   TEST: 02 NOTHING   |\nERROR : AttributeError')
    test = Recipe()
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

# Test:03 NO NAME [OK]
try:
    print('|   TEST: 03 NO NAME   |\nERROR : Attribute Error')
    test = Recipe('', 5, 145, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')


# Test:04 NOT STR NAME [OK]
try:
    print('|   TEST: 04 NOT STR NAME   |\nERROR : TypeError')
    test = Recipe(89, 5, 145, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

# Test: 05 NO LVL [OK]
try:
    print('|   TEST: 5 NO LVL   |\nERROR : AttributeError')
    test = Recipe('Pot au feu', 0 , 145, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

# Test:06 NOT INT LVL [OK]
try:
    print('|   Test:06 NOT INT LVL   |\nERROR : TypeError')
    test = Recipe('Pot au feu', '5', 145, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

# Test:07 NOT IN RANGE [OK]
try:
    print('|   Test:07 NOT IN RANGE   |\nERROR : AttributeError')
    test = Recipe('Pot au feu', 42, 145, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

# Test:08 NO TIME [OK]
try:
    print('|   TEST: 08 NO TIME   |\nERROR : AttributeError')
    test = Recipe('Pot au feu', 5, 0, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

# Test:09 NO STR TIME [OK]
try:
    print('|   TEST: 09 NO STR TIME   |\nERROR : TypeError')
    test = Recipe('Pot au feu', 5, '145', ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

# Test:10 NO NEGATIVE TIME [OK]
try:
    print('|   TEST: 10 NO NEGATIVE TIME   |\nERROR : AttributeError')
    test = Recipe('Pot au feu', 5, -145, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

# Test:11 NO LIST INGR [OK]
try:
    print('|   TEST: 11 NO LIST INGR   |\nERROR : AttributeError')
    test = Recipe('Pot au feu', 5, 145, [], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

# Test:12 NOT LIST LIST INGR [OK]
try:
    print('|   TEST: 12 NOT LIST LIST INGR   |\nERROR : TypeError')
    test = Recipe('Pot au feu', 5, 145, 'boeuf, carrotte, vin', \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

# Test:13 NO INGR [OK]
try:
    print('|   TEST: 13 NO INGR   |\nERROR : AttributeError')
    test = Recipe('Pot au feu', 5, 145, ['boeuf', '', 'vin'], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

# Test:14 NOT STR INGR[OK]
try:
    print('|   TEST: 14 NOT STR INGR   |\nERROR : TypeError')
    test = Recipe('Pot au feu', 5, 145, [29, 35, 15], \
    'Le plat préféré de ma femme', 'lunch')
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

# Test:15 NO DESCRIPTION [OK]
print('|   TEST: 15 NO DESCRIPTION   |\nERROR : NONE')
test = Recipe('Pot au feu', 5, 145, ['boeuf', 'carrotte', 'vin'], \
'', 'lunch')
print('CHECK: [OK]\n')

# Test:16 NOT STR DESCRIPTION [OK]
try:
    print('|   TEST: 10 NO NEGATIVE TIME   |\nERROR : TypeError')
    test = Recipe('Pot au feu', 5, 145, ['boeuf', 'carrotte', 'vin'], \
    800, 'lunch')
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

# Test:17 NO RECIPE TYPE [OK]
try:
    print('|   TEST: 17 NO RECIPE TYPE   |\nERROR : AttributeError')
    test = Recipe('Pot au feu', 5, 145, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', '')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

# Test:18 NOT STR RECIPE TYPE [OK]
try:
    print('|   TEST: 18 NOT STR RECIPE TYPE  |\nERROR : TypeError')
    test = Recipe('Pot au feu', 5, 145, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 42)
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

# Test:19 NOT GOOD RECIPE TYPE [OK]
try:
    print('|   TEST: 19 NOT GOOD RECIPE TYPE   |\nERROR : AttributeError')
    test = Recipe('Pot au feu', 5, 145, ['boeuf', 'carrotte', 'vin'], \
    'Le plat préféré de ma femme', 'souper')
    print('CHECK: [KO]\n')
except AttributeError:
    print('CHECK: [OK]\n')

## BOOK PART

print('####### BOOK PART ######\n')

# Test:20 NORMAL [?]
print('|   TEST: 20 NORMAL  |\nERROR : NONE')
book_test = Book()
print(book_test.name, '\n')
print(book_test.last_update, '\n')
print(book_test.creation_date, '\n')
print(book_test.recipes_list, '\n')

test2 = Recipe('Tarte au citron', 3, 45, ['citron', 'pate'], \
    'Mon plat préféré', 'dessert')
test3 = Recipe('Saumon creme', 3, 45, ['saumon', 'creme'], \
    'Notre plat préféré', 'lunch')
print('RECIPE RIGHT NOW :\n', str(test), '\n', str(test2), '\n', str(test3), \
'\n')

# TEST: 21 ADD RECIPE NORMAL [?]
print('|   TEST: 21 ADD RECIPE NORMAL  |\nERROR : NONE')
book_test.add_recipe(test)
print(book_test.name, '\n')
print(book_test.last_update, '\n')
print(book_test.creation_date, '\n')
print(book_test.recipes_list, '\n')

# TEST:22 ADD RECIPE NO RECIPE [?]
print('|   TEST: 22 ADD RECIPE NO RECIPE  |\nERROR : NRE')
book_test.add_recipe('')
print(book_test.name, '\n')
print(book_test.last_update, '\n')
print(book_test.creation_date, '\n')
print(book_test.recipes_list, '\n')

# TEST:23 ADD RECIPE NOT CLASS RECIPE [?]
try:
    print('|   TEST: 23 ADD RECIPE NOT CLASS RECIPE  |\nERROR : ERROR : \
TypeError')
    book_test.add_recipe(book_test)
    print('CHECK: [KO]\n')
except TypeError:
    print('CHECK: [OK]\n')

# TEST: 24 ADD_RECIPE UPDATE TIME [?]
print('|   TEST: 24 ADD RECIPE UPDATE TIME  |\nERROR : NONE')
print('OLD:', book_test.last_update)
book_test.add_recipe(test2)
book_test.add_recipe(test3)
print(book_test.name, '\n')
print(book_test.last_update, '\n')
print('NEW:', book_test.creation_date, '\n')
print(book_test.recipes_list, '\n')

# TEST 25 GET RECIPES NORMAL [?]
print('|   TEST: 25 GET RECIPES NORMAL  |\nERROR : NONE')
print('STARTER:')
book_test.get_recipes_by_types('starter')
print('LUNCH:')
book_test.get_recipes_by_types('lunch')
print('DESSERT:')
book_test.get_recipes_by_types('dessert')

# TEST: 26 GET RECIPES TYPE NO TYPE[?]
print('|   TEST: 26 GET RECIPES TYPE NO TYPE  |\nERROR : NRE')
book_test.get_recipes_by_types('')

# TEST 27 GET RECIPE NORMAL [?]
print('|   TEST: 27 GET RECIPES NORMAL  |\nERROR : NONE')
print('SAUMON:')
book_test.get_recipe_by_name('Saumon creme')
print('TARTE:')
book_test.get_recipe_by_name('Tarte au citron')
print('POT:')
book_test.get_recipe_by_name('Pot au feu')

#TEST: 28 GET RECIPE NAME NO NAME [?]
print('|   TEST: 28 GET RECIPE NAME NO NAME  |\nERROR : NRE')
book_test.get_recipe_by_name('')

