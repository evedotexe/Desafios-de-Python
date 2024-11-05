print("Olá! Bem-vindo ao cálculo de notas :D")

while True:
    try:
        nota1 = float(input("Insira a primeira nota: "))
        break 
    except ValueError:
        print("Não utilize letras! Somente números")

while True:
    try:
        nota2 = float(input("Insira a segunda nota: "))
        break 
    except ValueError:
        print("Não utilize letras! Somente números")

media = (nota1 + nota2) / 2

if media >= 10:
    print(f"Sua nota final foi {media}, Aprovado direto amigo!")
elif media >= 7:
    print(f"Sua nota final foi {media}, Aprovado!")
else:
    print(f"Sua nota final foi {media}, Reprovado.")
