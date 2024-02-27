import string

def convert_to_mayus_or_minus(text_mayus, text_minus):
    if text_mayus:
        return text_mayus.upper()
    elif text_minus:
        return text_minus.lower()
    
    letras_raras = 'áéíóúüñÁÉÍÓÚÜÑ'
    if text_mayus or text_minus != string.ascii_letters or ' ' or letras_raras:
        return 'Has ingresado caracteres no validos, intenta de nuevo.'

def main():
    while True:
        print(f'CONVERTIDOR DE TEXTO A MAYUSCULAS O MINUSCULAS')
        print('1. Convertir a mayusculas')
        print('2. Convertir a minusculas')
        print('3. Salir')
        choice = input('Enter your choice: ')

        if choice == '1':
            text = input('Enter the text to convert to mayus: ')
            print(convert_to_mayus_or_minus(text,''))
        elif choice == '2':
            text = input('Enter the text to convert to minus: ')
            print(convert_to_mayus_or_minus('',text))
        elif choice == '3':
            print('Exiting the program.')
            break
        else:
            print('Numero invalido, intenta de nuevo.')

if __name__ == '__main__':
    main()