import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    contador = 0
    categorias1 = []
    categorias = []
    while contador < len(dados):
        itens = dados[contador]['categoria']
        categorias1.append(itens)
        contador += 1
    for item in categorias1:
        if item not in categorias:
            categorias.append(item)
    return categorias    

def listar_por_categoria(dados, categoria):
    contador = 0
    categorias1 = []
    while contador < len(dados):
        itens = dados[contador]['categoria']
        item = dados[contador]['id']
        if itens == categoria:
            categorias1.append(item)
        contador += 1
    
    return categorias1   

def produto_mais_caro(dados, categoria):
    contador = 0
    categorias = []
    precos = []
    precos_final = []
    while contador < len(dados):
        itens = dados[contador]['categoria']
        produtos = dados[contador]
        if itens == categoria:
            categorias.append(produtos)
        for i in range(len(categorias)):
            preco = float(categorias[i]['preco'])
            produto = categorias[i]
            precos.append(preco)
            mais_caro = max(precos)
        contador += 1
    for x in range(len(categorias)):
        if float(categorias[x]['preco']) == mais_caro:
            precos_final.append(categorias[x]) 
        
    
    return precos_final
    
def produto_mais_barato(dados, categoria):
    contador = 0
    categorias = []
    precos = []
    precos_final = []
    while contador < len(dados):
        itens = dados[contador]['categoria']
        produtos = dados[contador]
        if itens == categoria:
            categorias.append(produtos)
        for i in range(len(categorias)):
            preco = float(categorias[i]['preco'])
            produto = categorias[i]
            precos.append(preco)
            mais_barato = min(precos)
        contador += 1
    for x in range(len(categorias)):
        if float(categorias[x]['preco']) == mais_barato:
            precos_final.append(categorias[x]) 
        
    
    return precos_final


def top_10_caros(dados):
    precos = []
    top10_final = []
    for x in range(len(dados)):
        preco = float(dados[x]['preco'])
        precos.append(preco)
    preco_ordenado = sorted(precos)
    top10 = preco_ordenado[-11:-1]
    for y in range(len(dados)):
        if float(dados[y]['preco']) in top10:
            top10_final.append(dados[y])

    return top10_final


def top_10_baratos(dados):
    precos = []
    top10_final = []
    for x in range(len(dados)):
        preco = float(dados[x]['preco'])
        precos.append(preco)
    preco_ordenado = sorted(precos)
    top10 = preco_ordenado[0:10]
    for y in range(len(dados)):
        if float(dados[y]['preco']) in top10:
            top10_final.append(dados[y])

    return top10_final



    

def menu(dados):
    opcao = int(input('Escolha uma das opções a seguir: \n1. Listar categorias\n2. Listar produtos de uma categoria\n3. Produto mais caro por categoria\n4. Produto mais barato por categoria\n5. Top 10 produtos mais caros\n6. Top 10 produtos mais baratos\n0. Sair\nDigite o número: '))
    
    while opcao != 0:
        if opcao == 1:
            print(listar_categorias(d))
        
        
        elif opcao == 2:
            categoria = input('Informe a categoria que seseja listar: ')
            print(listar_por_categoria(d, categoria))

        elif opcao == 3:
            categoria = input('Informe a categoria do produto: ')
            print(produto_mais_caro(d, categoria))

        elif opcao == 4:
            categoria = input('Informe a categoria do produto: ')
            print(produto_mais_barato(d, categoria))
        
        elif opcao == 5:
            print(top_10_caros(dados))

        elif opcao == 6:
            print(top_10_baratos(dados))

        else:
            print('Opção errada, favor digitar uma das opções a seguir: ')
        

        opcao = int(input('Escolha uma das opções a seguir: \n1. Listar categorias\n2. Listar produtos de uma categoria\n3. Produto mais caro por categoria\n4. Produto mais barato por categoria\n5. Top 10 produtos mais caros\n6. Top 10 produtos mais baratos\n0. Sair\nDigite o número: '))
        

    # Programa Principal - não modificar!
d = obter_dados()
menu(d)
