# Exercício de programação com if e comparação

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'o {primeiro_valor=} é maior do que o {primeiro_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'o {segundo_valor=} é maior do que o {primeiro_valor=}')
else:
    print(f'os valores "{primeiro_valor=}" e "{segundo_valor=}" são iguais')