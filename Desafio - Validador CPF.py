cpf = input('Digite um CPF: ')
caract = len(cpf)

if not cpf.isnumeric():
    print('CPF inválido! Digite apenas números!')
elif not caract == 11:
    print('CPF inválido. Digite um CPF válido!')
else:
    verificacao_cpf = list(cpf[:9])  # pega os 09 primeiros dígitos do CPF
    result_cpf = cpf[9:]  # pega os 02 últimos dígitos do CPF

#  cálculo conferir o primeiro dígito:

v1, v2, v3, v4, v5, v6, v7, v8, v9 = verificacao_cpf

valor1 = int(v1) * 10
valor2 = int(v2) * 9
valor3 = int(v3) * 8
valor4 = int(v4) * 7
valor5 = int(v5) * 6
valor6 = int(v6) * 5
valor7 = int(v7) * 4
valor8 = int(v8) * 3
valor9 = int(v9) * 2

result_1 = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7 + valor8 + valor9
# print(result_1)

dig_1 = 11 - (result_1 % 11)

if dig_1 > 9:
    dig_1 = 0

#  cálculo conferir o segundo dígito:

valor1 = int(v1) * 11
valor2 = int(v2) * 10
valor3 = int(v3) * 9
valor4 = int(v4) * 8
valor5 = int(v5) * 7
valor6 = int(v6) * 6
valor7 = int(v7) * 5
valor8 = int(v8) * 4
valor9 = int(v9) * 3
valor10 = dig_1 * 2

result_2 = valor1 + valor2 + valor3 + valor4 + valor5 + valor6 + valor7 + valor8 + valor9 + valor10
# print(result_2)

dig_2 = 11 - (result_2 % 11)

# validando o CPF:

novo_CPF = cpf[:9] + str(dig_1) + str(dig_2)
if novo_CPF == cpf:
    print(f'O cpf {cpf} foi validado com sucesso!')
else:
    print(f'O {cpf} é inválido!')