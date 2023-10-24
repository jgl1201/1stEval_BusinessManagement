ingredients = 'Mozarela, tomate y '
pizza_type = int(input('1: Pizza vegetariana. \n2: Pizza no vegetariana:'))

if pizza_type == 1:
    veg_ingredients = int(input('1: Pimiento \n2: Tofu:'))
    if veg_ingredients == 1:
        print(f'{ingredients}pimiento')
    elif veg_ingredients == 2:
        print(f'{ingredients}tofu')
    else:
        print('¿Tu eres tonto o te lo haces?')
elif pizza_type == 2:
    non_veg_ingredients = int(input('1: Peperoni \n2: Jamon \n3: Salmon:'))
    if non_veg_ingredients == 1:
        print(f'{ingredients}peperoni')
    elif non_veg_ingredients == 2:
        print(f'{ingredients}jamon')
    elif non_veg_ingredients == 3:
        print(f'{ingredients}salmon')
    else:
        print('¿Tu eres tonto o te lo haces?')
else: print('ERROR')