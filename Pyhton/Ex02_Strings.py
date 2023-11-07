def ex01(name, number):
    print((name + "\n") * number)

name = input("Introduce tu nombre: ")
number = int(input("Introduce un numero: "))
ex01(name, number)

def ex02(name):
    print(name.lower())
    print(name.upper())
    print(name.title())

full_name = input("Introduce tu nombre completo: ")
ex02(full_name)

def ex03(name):
    return len(name)

user_name = input("Introduce tu nombre: ")
print('Tu nombre tiene', ex03(user_name), 'letras')

def ex04(phone_number):
    print(phone_number[4:13])

phone_number = input("Introduce tu numero de telefono formato +prefijo-numero-extension: ")
ex04(phone_number)

def ex05(sentence):
    print(sentence[::-1])

sentence = input("Introduce una frase: ")
ex05(sentence)

def ex06(sentence, letter):
    print(sentence.replace(letter, letter.upper()))

sentence = input("Introduce una frase: ")
letter = input("Introduce una letra: ")
ex06(sentence, letter)

def ex07(mail):
    print(mail.split("@")[0] + '@ceu.es')

mail = input("Introduce tu correo: ")
ex07(mail)

def ex08(money):
    if len(money.split('.')[1]) > 2:
        print(f'{money} tiene más de dos decimales')
    else: 
        print(f'{money}€ son', money.split('.')[0], 'euros y', money.split('.')[1], 'centimos')

money = float(input("Introduce una cantidad de dinero (dos decimales): "))
ex08(str(money))

def ex09(date):
    day = date.split('/')[0]
    month = date.split('/')[1]
    year = date.split('/')[2]

    if len(day) == 1:
        day = day.zfill(2)
    if len(month) == 1:
        month = month.zfill(2)

    if ( (len(day) == 2 and day.isnumeric() and int(day) > 0) and 
         (len(month) == 2 and month.isnumeric() and int(month) > 0) and 
         (len(year) == 4 and year.isnumeric()) ):
        print(f'Dia: {day}, Mes: {month}, Año: {year}')
    else:
        print('Fecha invalida')

date = input("Introduce una fecha (dd/mm/yyyy): ")
ex09(date)

def ex10(products):
    list_products = products.split(",")
    for i in range (len(list_products)):
        print(f"El producto {i+1} es: {list_products[i]}")

products = input("Introduce los productos separados por comas: ")
ex10(products)

def ex11(product, price, units):
    print(f'{product} tiene un precio de {price:0>9.2f}€ y hay {units:0>4.0f} unidades, y el precio final es de {price * units:0>11.2f}€')