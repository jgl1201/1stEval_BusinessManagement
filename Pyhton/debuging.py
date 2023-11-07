def ex10(products):
    list_products = products.split(",")
    for i in range (len(list_products)):
        print(f"El producto {i+1} es: {list_products[i]}")

products = input("Introduce los productos separados por comas: ")
ex10(products)