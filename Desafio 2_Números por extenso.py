while True:
    try:
        numero = int(input("Insira o número: "))
        break 
    except ValueError:
        print("Utilize apenas números INTEIROS de 1 a 10")

print(f"Numero escolhido {numero}")

if numero == 1:
        print("1 -> Um!")

elif numero == 2:
        print("2 -> Dois!")

elif numero == 3:
        print("3 -> Três!")

elif numero == 4:
        print("4 -> Quatro!")

elif numero == 5:
        print("5 -> Cinco!")

elif numero == 6:
        print("6 -> Seis!")

elif numero == 7:
        print("7 -> Sete!")

elif numero == 8:
        print("8 -> Oito!")

elif numero == 9:
        print("9 -> Nove!")

elif numero == 19:
        print("10 -> Dez!")
    
