#01
user_name = str(input("Como te llamas: "))
print(f'Hola {user_name}')

#02
result = pow((3 + 2) / (2 * 5), 2) 
print(result)

#03
worked_hours = int(input('Introduce el numero de horas trabajadas: '))
hour_cost = int(input('Introduce el coste por hora: '))
print('Te corresponde una paga de', worked_hours * hour_cost, '€')

#04
def numberAdd(number):
    if number == 1: return 1
    return number + numberAdd(number-1)

number = abs(int(input('Introduce un numero positivo: ')))
print(numberAdd(number))

#05
def body_mass(weight, height):
    return weight / height

user_weight = int(input('Introduzca su peso en kg: '))
user_height = int(input('introduzca su estatura en cm: '))

print('Su IMC es:', body_mass(user_weight, user_height))

#06
number1 = int(input('Numero 1: '))
number2 = int(input('Numero 2: '))
print(number1, "/", number2, '=', int(number1 / number2), '; rest =', number1 % number2)

#07
initial_invest = int(input('Capital a invertir: '))
interest = float(input('Interes: '))
years = int(input('Años: '))

print('Capital final:', initial_invest + initial_invest * interest * years, '€')

#08
clown_weight = 112
doll_weight = 75
clown_number = int(input('Numero de payasos a enviar: '))
doll_number = int(input('Numero demuñecaas a enviar: '))

print('Peso total del paquete:', (clown_number * clown_weight + doll_number * doll_weight) / 1000, 'kg')

#09
def get_final_amount(quantity):
    return (quantity + (quantity * 0.04))

amount = float(input('Cantidad a depositar: '))
for i in range(0, 3):
    print('Cantidad del año', i + 1, '=', "{:.2f}".format(get_final_amount(amount), '€'))
    amount = get_final_amount(amount)

#10
bread_price = 3.49
discount_non_fresh_bread = 0.6
sold_nfb = int(input('Barras de pan duro vendidas: '))

print('Precio final:', "{:.2f}".format((bread_price * discount_non_fresh_bread) * sold_nfb), '€')