#REVISÃO: DESAFIO API em Alerta

endpoints = ["/login", "/produtos", "/pedidos"]

status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

#Funcao que verifica se um status code HTTP é sucesso
#200 á 299 = sucesso -> True
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

#Funcao detectar 2 erros seguidos nos codigos HTTP de um endpoint
def erros_seguidos(codigo_http):
    for i in range(len(codigo_http) -1 ):
        codigo_atual = codigo_http[i]
        prox_codigo = codigo_http[i + 1]
        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

# print(erros_seguidos(status[2]))

def analisar_endpoints(codigo_http):
    qtd_sucesso = 0

    for codigo in codigo_http:
        if eh_sucesso(codigo):
            qtd_sucesso += 1

    qtd_requisicoes = len(codigo_http)
    qtd_erro = qtd_requisicoes - qtd_sucesso

    percentual_sucesso = (qtd_sucesso / qtd_requisicoes) * 100

    tem_erros_seguidos = erros_seguidos(codigo_http)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucesso, qtd_erro, qtd_requisicoes, classificacao)

# print(analisar_endpoints(status[2]))


#Percorrendo toda a matriz
maior_qtd_erros = -1
endpoints_maior_erros = ''


for i in range(len(endpoints)):
    nome_endpoits = endpoints[i]
    codigo_endpoint = status[i]

    sucesso, erros, percentual, classificacao, = analisar_endpoints(codigo_endpoint)

    print(f'Endpoint: {nome_endpoits}')
    print(f'Código HTTP: {codigo_endpoint}')
    print(f'Sucesso: {sucesso}')
    print(f'Erros: {erros}')
    print(f'% de sucesso: {percentual:.1f}%')
    print(f'Classificação: {classificacao}')
    print('-' * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoints_maior_erros = nome_endpoits
    elif erros == maior_qtd_erros:
        endpoints_maior_erros += '' + nome_endpoits

print(f'Enpoint(s) com + erros: {endpoints_maior_erros} ({maior_qtd_erros})')