#Rafael Maluf
def arruma_linha(linha):
    return [e.strip() for e in linha.split(',')]

def uniao(conjunto1, conjunto2):
    resultado = set(conjunto1) | set(conjunto2)
    print(f"União: conjunto 1 {{{', '.join(conjunto1)}}}, conjunto 2 {{{', '.join(conjunto2)}}}. Resultado: {{{', '.join(sorted(resultado, key=lambda x: (conjunto1+conjunto2).index(x)))}}}")

def intersec(conjunto1, conjunto2):
    resultado = set(conjunto1) & set(conjunto2)
    print(f"Intersecção: conjunto 1 {{{', '.join(conjunto1)}}}, conjunto 2 {{{', '.join(conjunto2)}}}. Resultado: {{{', '.join(sorted(resultado, key=lambda x: (conjunto1+conjunto2).index(x)))}}}")

def dif(conjunto1, conjunto2):
    resultado = set(conjunto1) - set(conjunto2)
    print(f"Diferença: conjunto 1 {{{', '.join(conjunto1)}}}, conjunto 2 {{{', '.join(conjunto2)}}}. Resultado: {{{', '.join(sorted(resultado, key=lambda x: (conjunto1+conjunto2).index(x)))}}}")

def prod_cart(conjunto1, conjunto2):
    produto = [(e, e2) for e in conjunto1 for e2 in conjunto2]
    print(f"Produto Cartesiano: conjunto 1 {{{', '.join(conjunto1)}}}, conjunto 2 {{{', '.join(conjunto2)}}}. Resultado: {produto}")

def abrir_txt(txt_teste):
    with open(txt_teste, 'r', encoding='utf8') as arquivo:
        linhas = [l.strip("\n") for l in arquivo]
        num_op = int(linhas[0])
        idx1 = 2
        idx2 = 3
        idx_op = 1
        for _ in range(num_op):
            conjunto1 = arruma_linha(linhas[idx1])
            conjunto2 = arruma_linha(linhas[idx2])

            if linhas[idx_op] == 'U':
                uniao(conjunto1, conjunto2)
            elif linhas[idx_op] == 'I':
                intersec(conjunto1, conjunto2)
            elif linhas[idx_op] == 'D':
                dif(conjunto1, conjunto2)
            else:
                prod_cart(conjunto1, conjunto2)

            idx1 += 3
            idx2 += 3
            idx_op += 3

txt_teste = "teste1.txt"
abrir_txt(txt_teste)

#para testar todos os meus arquivos, troca o txt_teste pelos outros nomes.
#para testar um especifico, add ele na pasta do codigo.
#teste1.txt
#teste2.txt
#teste3.txt
