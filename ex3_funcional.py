strings = [input(), input(), input()]

strings_caixa_alta = list(map(str.upper, strings))

string_maior_tamanho = max(strings, key=len)

print("Strings em caixa alta:", strings_caixa_alta)
print("String com maior quantidade de caracteres:", string_maior_tamanho)