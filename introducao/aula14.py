# Formatação de string com o método format

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
# quando uma funcao esta dentro de um objeto, esta funcao é chamado de método.
formato = string.format(
    nome1=a, nome2=b, nome3=c   # parametro nomeado é quando da um nome para as coisas dentro da chamada das funções
)
print(formato)


nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))