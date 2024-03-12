import requests
import json

def listas():
    busca = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    request_busca = requests.get(busca)
    response = request_busca.json()
    lista = response['meals']
    for i, food in enumerate(lista):
        print(i + 1 ,food['strArea'])
    return lista

def cardapio(nome):
    busca = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={nome}"
    request_busca = requests.get(busca)
    json_result = json.loads(request_busca.content)['meals']
    if json_result == None:
        print("Infelizmente não há cardapio para esse tipo de comida")
        return None
    else:
        for i in json_result:
            print()
            print(f"Clique aqui para ver a comida: {i['strMealThumb']}")
            print()
            print(f"Numéro do pedido {i['idMeal']}, {i['strMeal']}")
    return json_result
    

def categorias():
    busca_categoria = "https://www.themealdb.com/api/json/v1/1/categories.php"
    request_categoria = requests.get(busca_categoria)
    json_result = json.loads(request_categoria.content)['categories']
    for i in json_result:
        print()
        print(i['strCategory'])
        print()
        print(i['strCategoryDescription'])
    return json_result

def cardapio2(pesquisa):
    busca_categoria = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={pesquisa}"
    request_categoria = requests.get(busca_categoria)
    json_result = json.loads(request_categoria.content)['meals']
    if json_result == None:
        print("Infelizmente não há cardapio para esse tipo de comida")
        return None
    else:
        for i in json_result:
            print()
            print(f"Clique aqui para ver a comida: {i['strMealThumb']}")
            print()
            print(f"Numéro do pedido {i['idMeal']}, {i['strMeal']}")
    return json_result

pesquisar = input("Deseja ver nosso cardarpio por categoria ou por pais: ")
if pesquisar.isalpha():
    if pesquisar == "categoria":
        categorias()
        print()
        pesquisa = input("Digite o tipo de iguaria que deseja ? ")
        if pesquisa.isalpha():
            cardapio2(pesquisa)
    elif pesquisar == "pais":
        listas()
        print()
        pesquisa = input("Digite o tipo de iguaria que deseja ? ")
        if pesquisa.isalpha():
            cardapio(pesquisa)
    else:
        print("Apenas comida por categorias ou pais")
else:
    print("Digite apenas letras")
         