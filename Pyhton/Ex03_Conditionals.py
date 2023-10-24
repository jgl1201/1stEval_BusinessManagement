#01
def is_adult(age):
    return age >= 18

user_age = int(input('Edad: '))
if is_adult(user_age): print('Eres mayor de edad')
else: print('Niñato')

#02
def passwd_Match(passwd, user_pass):
    return passwd == user_pass

password = 'password'
user_password = str(input('Contraseña: '))

if passwd_Match(password.lower, user_password.lower) : print('Contraseña correcta')
else: print('Contraseña incorrecta')

#03
def divide(number1, number2):
    try:
        return number1 / number2
    except ValueError: 
        print("Algo ha ido mal")

number1 = int(input('Introduce Dividendo: '))
number2 = int(input('Introduce Divisor: '))
print(divide(number1, number2))

#04
def is_even(number):
    return number % 2 == 0

number = int(input('Introduce un numero:'))
if(is_even(number)): print('Par')
else: print('Impar')

#05
def must_tribute(age, income):
    return age > 16 and income >= 1000.0

age = int(input('Introduzca su edad:'))
income = float(input('Introducta sus ingresos mensuales:'))
if(must_tribute(age, income)): print('Debes tributar')
else: print('No debes tributar')

#06
def define_group(name, sex):
    # Mujeres de la A a la M
    if((name[0].lower() >= 'a' or name[0].lower() < 'n') and (sex.lower() == 'm')): return 'Grupo A'
    # Hombres de la N a la Z
    if((name[0].lower() >= 'n' or name[0].lower() <= 'z') and (sex.lower() == 'h')): return 'Grupo A'
    return 'Grupo B'

name = str(input('Introduce tu nombre:'))
sex = str(input('Pon M si eres mujer, H si eres hombre:'))
define_group(name, sex)

#07
def get_tax(rent):
    if rent < 10000: 
        return '5%'
    if rent >= 10000 and rent < 20000:
        return '15%'
    if rent >= 20000 and rent < 35000:
        return '20%'
    if rent >= 35000 and rent < 60000:
        return '30%'
    return '45%'

rent = int(input('Introduce tu renta anual: '))
print(get_tax(rent))

#08
def get_employee_points(points):
    salary = 2400 * points
    if points < 0.0 or points > 0.4: return 'Puntuacion invalida'
    if points == 0.0: return f'Inaceptable, sueldo: {salary}'
    if points == 0.4: return f'Aceptable, sueldo: {salary}'
    return f'Meritorio, sueldo: {salary}'

employee_points = float(input('Introduce tus puntos: '))
print(get_employee_points(employee_points))

#09
def calculate_entry_price(age):
    if age < 4:
        return 'Entrada: GRATIS'
    if (age >= 4) and (age <= 18):
        return 'Entrada: 5€'
    return 'Entrada: 10€'

entry_age = int(input('Edad: '))
print(calculate_entry_price(entry_age))

#10
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