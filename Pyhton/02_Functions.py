def defineTemperature(temperature):
    if temperature < 20:
        if temperature < 10: print("Blue lever")
        else: print("Yellow level")
    elif temperature < 30: print("Orange level")
    else: print("Red level")

num = num1 = num2 = 5
print(num, num1, num2)

temperature = 43
defineTemperature(temperature)