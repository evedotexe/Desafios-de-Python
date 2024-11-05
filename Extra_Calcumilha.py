print("BEM VINDO A CALCUMILHA!")

while True:
    try:
        numero1 = float(input("COLOCA O PRIMEIRO NUMERO CARALHO: "))
        break 
    except ValueError:
        print("Puta q pariu man tu eh burro, usa NUMERO")

while True:
    try:
        operacao = str(input("A OPERAÇÃO FUDIDO: "))
        break 
    except ValueError:
        print("Utilize esses daqui cacetinho: +, -, * e /")

while True:
    try:
        numero2 = float(input("AGR O SEGUNDO NUMERO DESGRAÇADO: "))
        break 
    except ValueError:
        print("CARA eu me RECUSO a calcular se tu nao usa NUMERO")


soma = (numero1 + numero2)
subtracao = (numero1 - numero2)
multiplicacao = (numero1 * numero2)
divisao = (numero1 / numero2)
media = ((numero1 + numero2) /2)

if operacao == "+":
    print(f"VAI SE FUDER COMO {soma} E TU NAO FAZ DE CABEÇA? BURRO DO KRL")

elif operacao == "-":
    print(f"caceta! deu {subtracao} arrombado")

elif operacao == "*":
    print(f"seu valor deu {multiplicacao} ,filho da puta")

elif operacao == "/":
    print(f"Amiguinho... deu {divisao} esta merda, esperava mais de vc DESGRAÇADO")

elif operacao == "media":
    print(f"desgraçado filho da puta arrombado {media} DEU ESSA POOORRA")