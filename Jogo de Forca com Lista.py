secreto = 'avenida'
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra por vez!')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'A palavra secreta contém a letra "{letra}"')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta!')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns, você ganhou, a palavra secreta é "{secreto_temporario.upper()}"')
        break
    else:
        print(secreto_temporario)

    if letra not in secreto:
        chances -= 1
    print(f'Você tem {chances} chances!')
print()
