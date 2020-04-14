class Recipe:
    def __init__(self, name = '', cooking_lvl = 0, cooking_time = 0,\
    ingredients = [], description = 'None', recipe_type = ''):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, n):
        if not n:
            raise AttributeError('No empty name')
        if not isinstance(n, str):
            raise TypeError('Only string are allowed for name')
        self._name = n
    
    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, lvl):
        if not lvl:
            raise AttributeError('No empty cooking_lvl')
        if not isinstance(lvl, int):
            raise TypeError('Only int are allowed for cooking_lvl')
        if lvl < 1 or lvl > 5:
            raise AttributeError('cooking_lvl must be between 1 and 5')
        self._cooking_lvl = lvl

    @property
    def cooking_time(self):
        return self._cooking_time
    
    @cooking_time.setter
    def cooking_time(self, time):
        if not time:
            raise AttributeError('No empty cooking_time')
        if not isinstance(time, int):
            raise TypeError('Only int are allowed for cooking_time')
        if time <= 0:
            raise AttributeError('No negative number for cooking_time')
        self._cooking_time = time
    
    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, i):
        if not i:
            raise AttributeError('No empty ingredient\'s list')
        if not isinstance(i, list):
            raise TypeError('Only list are allowed for ingredient\'s list')
        for element in i:
            if not element:
                raise AttributeError('No empty list\'s\
                ingredient')
            if not isinstance(element, str):
                raise TypeError('Only string are allowed for list\'s\
                ingredient')
        self._ingredients = i
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, desc):
        if not isinstance(desc, str):
            raise TypeError('Only string are allowed for description')
        self._description = desc

    @property
    def recipe_type(self):
        return self._recipe_type
    
    @recipe_type.setter
    def recipe_type(self, rtype):
        if not rtype:
            raise AttributeError('No empty recipe_type')
        if not isinstance(rtype, str):
            raise TypeError('Only string are allowed for recipe_type')
        if not rtype == 'starter' and not rtype == 'lunch' \
        and not rtype == 'dessert':
            raise AttributeError('recipe_type can only be starter, lunch or \
            dessert')
        self._recipe_type = rtype
    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = 'Name : {}\nLVL : {}/5\nTIME : {}\nIngredients : {}\n\
Description: {}\nType : {}'\
        .format(self.name, self.cooking_lvl, self.cooking_time,
        self.ingredients, self.description, self.recipe_type)
        return txt
