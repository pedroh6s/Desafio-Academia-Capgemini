n = 6

'''Como o número de caracteres por linha é uma constante, no caso o valor de n, o cálculo é bem
fácil, basta imprimir um número de espaços complementar ao número de asteriscos.
E é de vital importância concatenar o resultado, outras formas de escrita dessa parte do código
podem adicionar um indesejado espaço extra.
'''
for i in range(1, n + 1):
    print(' '*(n - i) + '*'*i)
