# Conversor de Unidades: Graus Celsius e Fahrenheit

def menu():
    print('***Programa para Conversão de Temperatura***')
    print('   1. Converter Celsius para Fahrenheit')
    print('   2. Converter Fahrenheit para Celsius')

def celsius_fahrenheit():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def fahrenheit_celsius():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

if __name__=='__main__':
    menu()
    numero = input('Escolha o número de conversão que deseja realizar: ')

    if numero == '1':
        celsius_fahrenheit()

    if numero == '2':
        fahrenheit_celsius()